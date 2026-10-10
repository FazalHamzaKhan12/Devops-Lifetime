# TrainWithShubham - Practical Python

Hands-on Python scripting focused on DevOps essentials: system resource monitoring (`psutil`), REST API services (`fastapi`), API consumption (`requests`), defensive error handling (`try-except`), and AWS cloud automation (`boto3`).

## About This Course

- **Course:** TrainWithShubham Python Live/Class Series
- **Instructor / Channel:** Shubham Londhe ([TrainWithShubham](https://www.youtube.com/@TrainWithShubham))
- **Focus:** Practical Python application for systems engineering—moving rapidly from language basics to OS metrics, HTTP APIs, and cloud services.
- **Why It Is Useful:** This course shifts Python from abstract programming concepts into practical DevOps tooling. Instead of solving toy math problems, scripts monitor CPU and RAM usage, spin up lightweight metric-reporting APIs, and upload artifacts to AWS S3.
- **Where It Fits in the DevOps Journey:** This represents Step 02. It builds on the basics learned in Apna College and introduces the real-world libraries (`psutil`, `boto3`, `requests`, `fastapi`) used daily by DevOps engineers.

## Topics Covered

| Status | Topic | Details |
|---|---|---|
| ✅ | Basic Syntax & Variables | Output formatting, typed variables, user details |
| ✅ | Core Collections | Lists, tuples, dictionaries, and sets applied to cloud provider lists |
| ✅ | System Monitoring (`psutil`) | Measuring CPU %, memory %, and disk usage |
| ✅ | Conditional Health Thresholds | Alerting when memory or CPU surpasses defined limits |
| ✅ | REST API Consumption (`requests`) | Fetching JSON payloads, timeouts, and `raise_for_status()` |
| ✅ | Lightweight API Services (`fastapi`) | Creating endpoints for `/metrics`, `/server-info`, and `/user` |
| ✅ | Defensive Scripting (`try-except`) | Handling `TypeError`, `ZeroDivisionError`, and unexpected exceptions |
| ✅ | Modular Code Design | Organizing utility functions into helper modules and importing them |
| ✅ | AWS Cloud Automation (`boto3`) | Listing S3 buckets and uploading local files to cloud storage |

## Practical Examples

| Script / Project | Purpose | Python Concept | Why It Is Useful |
|---|---|---|---|
| [cpu_check.py](Day-02/projects/cpu_check.py) | Evaluates CPU percentage against usage bands | `input()`, conditionals (`if`/`elif`/`else`) | Basic logic for server capacity alerting |
| [health_check.py](Day-02/projects/health_check.py) | Continuously samples CPU load 5 times | `psutil.cpu_percent(interval=1)`, `for` loop | Monitoring system stability over time |
| [real_cpu_check.py](Day-02/projects/real_cpu_check.py) | Inspects actual RAM and CPU percentages | `psutil.virtual_memory()`, `os.system()` | Real-time trigger for automated remediation |
| [systemdetails](Day-02/projects/systemdetails/show_system.py) | Collects CPU, memory, and disk in a structured dict | Custom module import (`system_utils`), dictionaries | Modular telemetry collection for monitoring agents |
| [01_api.py (FastAPI)](Day-03/fastapi/01_api.py) | Microservice serving `/metrics` and `/server-info` | FastAPI, decorators (`@app.get`), JSON response | Building internal health check and telemetry APIs |
| [01_s3_utils.py](Day-04/01_s3_utils.py) | Lists AWS S3 buckets filtered by substring pattern | `boto3.resource('s3')`, iteration | Auditing and inventorying cloud storage assets |
| [01_s3_upload.py](Day-05/01_s3_upload.py) | Uploads local script files to an AWS S3 bucket | `boto3.client('s3')`, `.upload_file()` | Automating artifact backups to the cloud |
| [03_system_health.py](Day-05/03_system_health.py) | Comprehensive health report for CPU, RAM, disk | Dictionaries, thresholds, functions, status formatting | Production-grade server health audit script |
| [04_try_except.py](Day-05/04_try_except.py) | Safely handles division and type errors | `try` / `except` / `finally` | Ensuring automation scripts don't crash unexpectedly |
| [02_call_api.py](Day-06/02_call_api.py) | Calls a REST endpoint, validates HTTP status | `requests.get()`, `response.raise_for_status()` | Consuming webhook APIs, CI/CD status, or remote services |

## Python Concepts Learned

- **External Libraries & Virtual Environments:** Installing and importing third-party modules such as `psutil`, `requests`, `fastapi`, and `boto3`.
- **System Metrics Extraction:** Utilizing OS hooks through `psutil` to inspect hardware and process metrics.
- **Microservices with FastAPI:** Creating route handlers using Python decorators (`@app.get()`, `@app.post()`) that automatically serialize Python dictionaries into JSON responses.
- **Exception Handling:** Using defensive blocks (`try`, `except Exception as e`, `finally`) to catch failures gracefully instead of halting execution.
- **AWS SDK Integration:** Using `boto3` client and resource interfaces to programmatically interact with Amazon S3.
- **Modular Project Structure:** Splitting logic into utility modules (`system_utils.py`, `calculator.py`) and importing them cleanly into entrypoint scripts (`show_system.py`, `main.py`).

## DevOps Relevance

- **Infrastructure Monitoring:** The scripts in `Day-02/projects/` and `Day-05/03_system_health.py` illustrate how automated agents monitor server health without third-party agent overhead.
- **Custom Health APIs:** The FastAPI implementation in `Day-03/fastapi/01_api.py` demonstrates how DevOps engineers expose custom `/health` and `/metrics` endpoints for Prometheus or load balancers.
- **Cloud Backup & Disaster Recovery:** The Boto3 scripts in `Day-04` and `Day-05` illustrate how automation replaces manual AWS console uploads for deployment artifacts and configuration snapshots.
- **Fault-Tolerant Automation:** Production automation cannot fail silently or terminate midway; defensive exception handling ensures errors are caught, logged, and handled cleanly.

## Learning Notes

- `psutil.cpu_percent(interval=1)` blocks for 1 second to compare CPU times across that duration; calling it with `interval=0` or without arguments returns 0.0 or an instantaneous non-representative value.
- When calling external APIs via `requests.get()`, always pass a `timeout` argument and invoke `.raise_for_status()` to catch HTTP 4xx/5xx errors.
- Boto3 requires AWS credentials to be configured via the AWS CLI (`~/.aws/credentials`), environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`), or an IAM role.

## Projects / Exercises

### Day 01 — Getting Started
- [01_print.py](Day-01/01_print.py)
- [02_variables.py](Day-01/02_variables.py)

### Day 02 — Collections, Control Flow & System Projects
- [03_list-dic-tuple-set.py](Day-02/03_list-dic-tuple-set.py)
- [04_conditional.py](Day-02/04_conditional.py)
- [05_loop.py](Day-02/05_loop.py)
- [01_api_using.py](Day-02/api_python/01_api_using.py)
- [cpu_check.py](Day-02/projects/cpu_check.py)
- [health_check.py](Day-02/projects/health_check.py)
- [real_cpu_check.py](Day-02/projects/real_cpu_check.py)
- [show_system.py](Day-02/projects/systemdetails/show_system.py) & [system_utils.py](Day-02/projects/systemdetails/system_utils.py)

### Day 03 — FastAPI Telemetry Microservice
- [01_api.py](Day-03/fastapi/01_api.py)

### Day 04 — AWS Boto3 Basics
- [01_s3_utils.py](Day-04/01_s3_utils.py)

### Day 05 — S3 Uploads, Error Handling & System Health
- [01_s3_upload.py](Day-05/01_s3_upload.py)
- [03_system_health.py](Day-05/03_system_health.py)
- [04_try_except.py](Day-05/04_try_except.py)
- [main.py](Day-05/main_practice/main.py) & [calculator.py](Day-05/main_practice/calculator.py)

### Day 06 — Collections & REST API Consumer
- [01_collection.py](Day-06/01_collection.py)
- [02_call_api.py](Day-06/02_call_api.py)

## What I Learned

Transitioned from basic programming exercises to writing functional DevOps scripts. Gained hands-on experience querying system metrics with `psutil`, deploying a metrics REST API with `fastapi`, integrating with AWS S3 using `boto3`, and writing resilient code with structured error handling.

## Next Step

Proceed to [03-TrainWithShubham-Python-for-DevOps](../03-TrainWithShubham-Python-for-DevOps/README.md) for deep-dive automation workflows, including automated directory backup pipelines (`shutil`, `datetime`) and AWS S3 automation.