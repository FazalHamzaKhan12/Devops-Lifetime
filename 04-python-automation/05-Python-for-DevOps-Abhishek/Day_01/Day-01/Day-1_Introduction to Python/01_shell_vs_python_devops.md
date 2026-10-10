# Shell vs Python Scripting for DevOps: The Practical Guide

A simple, no-nonsense comparison to help you choose the right tool for any DevOps task.

---

## ⚡ Quick Rule of Thumb

| Question | Tool | Why? |
| :--- | :--- | :--- |
| **"Am I chaining Linux commands together?"** | **Bash / Shell** | Native OS control, zero overhead, fast execution. |
| **"Do I need logic, APIs, JSON, or Cloud SDKs?"** | **Python** | Robust data structures, error handling, maintainable code. |

> **Mental Model:**
> * **Shell** = *"Control the operating system."*
> * **Python** = *"Build automation with logic."*

---

## 1. Shell Scripting (Bash)

### What it is
A sequence of native Linux/Unix commands saved in an executable file.

### Best used for:
1. **System Administration:** Managing files, system services (`systemctl`), user permissions, and disk cleanup.
2. **CLI Chaining:** Running tools one after another (`docker`, `kubectl`, `git`, `tar`).
3. **Quick CI/CD Steps:** Simple build/deploy triggers inside pipeline runners.
4. **Basic Log/Text Filtering:** Searching or piping logs with `grep`, `awk`, `sed`, `cut`.
5. **Environment Setup:** Exporting environment variables and setting paths.

### Production Example: Quick Deployment & Health Check
```bash
#!/usr/bin/env bash
set -euo pipefail  # Exit immediately on errors or unbound variables

echo "[+] Pulling latest images..."
docker compose pull

echo "[+] Restarting services..."
docker compose down
docker compose up -d

echo "[+] Checking service status..."
docker compose ps
```

### When Shell starts to hurt:
* Parsing nested JSON or YAML.
* Handling complex data structures (nested maps, lists of dicts).
* Requiring clean cross-platform execution (Linux vs macOS vs Windows).
* Scripts exceeding ~100–150 lines with heavy conditional branches.

---

## 2. Python Scripting

### What it is
A high-level programming language with rich standard libraries and third-party packages.

### Best used for:
1. **Cloud & SDK Automation:** Interacting with AWS (Boto3), Azure SDK, or GCP client libraries.
2. **REST API Integrations:** Communicating with GitHub, Jira, Slack, Datadog, or internal APIs via `requests` or `httpx`.
3. **Structured Data Processing:** Parsing and transforming JSON, YAML, CSV, or XML data cleanly.
4. **Resilient Error Handling:** `try / except` blocks, structured logging, and fallback mechanisms.
5. **Scalable Codebases:** Splitting code into reusable functions, classes, and packages.

### Production Example: AWS EC2 Inventory & Slack Alert
```python
import os
import boto3
import requests

ec2 = boto3.client("ec2", region_name="us-east-1")
webhook_url = os.environ.get("SLACK_WEBHOOK_URL")

try:
    # Fetch stopped instances
    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["stopped"]}]
    )
    
    stopped_instances = [
        inst["InstanceId"]
        for res in response["Reservations"]
        for inst in res["Instances"]
    ]

    print(f"Found {len(stopped_instances)} stopped instances.")

    # Notify Slack if any found
    if stopped_instances and webhook_url:
        payload = {"text": f"⚠️ Found stopped EC2 instances: {', '.join(stopped_instances)}"}
        requests.post(webhook_url, json=payload, timeout=5)

except Exception as err:
    print(f"[ERROR] AWS automation failed: {err}")
    exit(1)
```

---

## 3. Side-by-Side Comparison

| Feature | Shell (Bash) | Python |
| :--- | :--- | :--- |
| **Primary Strength** | OS-level command execution | Application logic, APIs & data |
| **JSON / Data Parsing** | Awkward (requires `jq` or regex) | Native (`import json`) |
| **Cloud Automation** | AWS CLI (shell string parsing) | Boto3 (Python SDK with full objects) |
| **Error Handling** | Exit codes (`set -e`, `$?`) | Structured `try/except` exceptions |
| **Speed to Write** | Instant for 2–10 command tasks | Requires slight boilerplate |
| **Cross-Platform** | Unix/Linux only (Git Bash/WSL on Windows) | Runs on Linux, macOS, and Windows |
| **Maintainability** | Degrades fast as script grows | High; supports OOP, modules, tests |

---

## 4. How They Work Together in Real DevOps

In production, you don't pick one exclusively—you combine them:

```text
CI/CD Pipeline / Linux Cron
           │
           ▼
     [ Bash Script ]  <── Handles environment vars, runs docker, initiates execution
           │
           ▼
    [ Python Script ] <── Talks to AWS Boto3, parses JSON, sends Slack alert
           │
           ▼
     [ Exit Code ]    <── Returns status code (0 = success, 1 = failure) back to Bash
```

### Real Example:
```bash
#!/usr/bin/env bash
set -e

# 1. Shell handles environment preparation
export AWS_REGION="us-east-1"
source /opt/venv/bin/activate

# 2. Python executes complex logic and API calls
python3 /opt/scripts/audit_infrastructure.py

# 3. Shell checks exit status and cleans up
echo "Audit complete with status code $?"
```

---

## 5. Summary Cheat Sheet

* **Use Shell when:**
  * You are just automating what you normally type in the terminal.
  * Moving files, restarting systemd units, running Docker commands.
  * Writing entrypoints for Docker containers (`entrypoint.sh`).

* **Use Python when:**
  * You need to call external HTTP APIs or Cloud SDKs.
  * You need loops inside loops, mathematical logic, or complex conditions.
  * You need to generate reports (JSON, CSV, Excel, HTML).
  * Your script needs unit tests or modular packaging.
