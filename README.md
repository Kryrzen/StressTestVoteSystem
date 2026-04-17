# StressTestVoteSystem: Lab Challenge

**Objective:** Try to figure out the webserver and give yourself as much votes as you can.

---

## Overview
The **StressTestVoteSystem** is an educational project designed to demonstrate how asynchronous programming and TCP persistence can be used to test the limits of a web application. 

This lab uses "RigVotes.py", a script built with the aiohttp library. Unlike traditional "synchronous" scripts that send one request and wait for a response, this script utilizes an **Asynchronous Event Loop** to manage thousands of simultaneous connections.

---

## Core Networking Concepts
This challenge highlights three critical pillars of modern network engineering:

| Concept | Description |
| :--- | :--- |
| **TCP Persistence** | Uses "TCPConnector" to keep connections open (Keep-Alive), avoiding the overhead of repeated 3-way handshakes. |
| **Concurrency** | Demonstrates how a single thread can manage thousands of tasks by yielding control while waiting for I/O (Network) responses. |
| **Resource Exhaustion** | Illustrates the "File Descriptor" limit in Operating Systems, where each socket is treated as an open file. |

---

## Setup & Execution

### 1. Prerequisites
Ensure you have Python 3.7+ installed. Verify your version:
```bash
python --version
```
### 2. Install Dependencies
This script requires the aiohttp library to handle non-blocking HTTP requests:
```bash
pip install aiohttp
```

### 3. Configuration
Open RigVotes.py and ensure the target parameters match your lab environment:

URL: The endpoint of the voting server (http://targetip/vote.php)

CANDIDATE_ID: The ID of the candidate you are targeting.

CONCURRENT: The number of simultaneous streams.

### 4. Launch the Challenge
Run the script from your terminal:
```bash
python RigVotes.py
```

## Troubleshooting & Observations
Connection Timeouts: If the server is overwhelmed, you will see speed (votes/sec) drop as the server stops responding to the "firehose" of data.

OSError [Errno 24]: This means you've hit your OS limit for open files. Lower the CONCURRENT variable to 500 or use ulimit -n to increase your system limits.

Status 503/504: These HTTP codes indicate the server's backend (PHP or Database) has crashed under the load.

Educational Disclaimer: This tool is strictly for authorized testing in a controlled lab environment. Unauthorized use against systems you do not own is illegal and unethical.
