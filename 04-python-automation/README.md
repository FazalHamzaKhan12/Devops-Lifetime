# Python for DevOps

A structured, practical Python learning journey focused on automation, operating system interaction, REST APIs, cloud SDKs, and DevOps engineering.

---

## About

This repository documents my hands-on journey learning **Python for DevOps and Cloud Engineering**. 

Coming from a programming background in **C++, C#, and Object-Oriented Programming (OOP)**, my primary goal is not just learning syntax, but understanding how Python is applied to eliminate manual sysadmin toil, monitor infrastructure health, automate backup pipelines, interact with REST APIs, and manage cloud resources programmatically.

Every script in this repository represents authentic, hands-on practice written while studying carefully selected courses and workshops.

---

## Learning Journey

The repository is organized into five sequential milestones:

| # | Course / Resource | Primary Focus | Status | Documentation |
|---|---|---|---|---|
| **01** | [Apna College Python](01-Apna-College-Python/) | Core syntax, data types, operators, collections, and functions | ✅ Completed | [01 README](01-Apna-College-Python/README.md) |
| **02** | [TrainWithShubham Python](02-TrainWithShubham-Python/) | System metrics (`psutil`), REST APIs (`fastapi`, `requests`), S3 uploads (`boto3`) | ✅ Completed | [02 README](02-TrainWithShubham-Python/README.md) |
| **03** | [TrainWithShubham DevOps Workshop](03-TrainWithShubham-Python-for-DevOps/) | OS commands (`os.system`), automated directory backups (`shutil`), AWS S3 | ✅ Completed | [03 README](03-TrainWithShubham-Python-for-DevOps/README.md) |
| **04** | [Python OOP Deep-Dive](04-Python-OOP/) | OOP paradigms, encapsulation, inheritance, polymorphism, infrastructure modeling | ✅ Completed | [04 README](04-Python-OOP/README.md) |
| **05** | [Python for DevOps - Abhishek Veermalla](05-Python-for-DevOps-Abhishek/) | Enterprise DevOps use cases, log processing, advanced error recovery | 🔄 In Progress | [05 README](05-Python-for-DevOps-Abhishek/README.md) |

---

## Learning Roadmap

```text
Python Fundamentals (Variables, Types, Conditions, Loops)
       │
       ▼
Data Structures (Lists, Tuples, Sets, Dictionaries)
       │
       ▼
Modular Functions & Standard Library Modules
       │
       ▼
Object-Oriented Programming (Classes, Inheritance, Aggregation)
       │
       ▼
Defensive Error Handling (try-except-finally blocks)
       │
       ▼
OS & File System Automation (os, shutil, datetime, archiving)
       │
       ▼
System Health Monitoring & Telemetry (psutil, threshold alerting)
       │
       ▼
REST APIs & Web Services (requests, FastAPI endpoints)
       │
       ▼
Cloud Automation & SDKs (AWS Boto3, S3 storage operations)
       │
       ▼
Enterprise Incident Automation & CI/CD Scripting (Upcoming)
```

---

## DevOps Python Skills

The scripts in this repository demonstrate practical capabilities across multiple DevOps domains:

### 1. System Health Monitoring & Telemetry
- Querying live CPU %, virtual memory %, and disk usage via `psutil`.
- Comparing metrics against configurable thresholds and emitting health audit summaries.
- Script reference: [`03_system_health.py`](02-TrainWithShubham-Python/Day-05/03_system_health.py)

### 2. Filesystem & Backup Automation
- Generating automated, timestamped `.tar.gz` and `.zip` archives using `shutil` and `datetime`.
- Cross-platform path handling with `os.path.join()`.
- Script reference: [`backup.py`](03-TrainWithShubham-Python-for-DevOps/Day_02/backup_usingpy/backup.py)

### 3. Cloud Infrastructure Automation (AWS SDK)
- Connecting to AWS services programmatically using `boto3`.
- Discovering, auditing, and filtering S3 buckets by naming pattern.
- Uploading build artifacts and files directly to S3 buckets.
- Script reference: [`01_s3_upload.py`](02-TrainWithShubham-Python/Day-05/01_s3_upload.py) & [`s3_buckets_names.py`](03-TrainWithShubham-Python-for-DevOps/Day-03/boto3_practice/s3_buckets_names.py)

### 4. REST APIs & Microservices
- Building lightweight internal telemetry APIs with `fastapi` to expose `/metrics` and `/server-info`.
- Consuming external REST APIs defensively with `requests`, timeouts, and HTTP status verification (`raise_for_status()`).
- Script reference: [`01_api.py`](02-TrainWithShubham-Python/Day-03/fastapi/01_api.py) & [`02_call_api.py`](02-TrainWithShubham-Python/Day-06/02_call_api.py)

### 5. Infrastructure Modeling via OOP
- Modeling physical/virtual servers, web servers, and deployment pipelines using Python classes.
- Encapsulating configuration state and managing server lifecycle actions (`start()`, `stop()`, `deploy()`).
- Designing reusable utilities with static methods (e.g., IPv4 format validator).
- Script reference: [`05_devops_serverPractice.py`](04-Python-OOP/Day-02/05_devops_serverPractice.py) & [`05_@method_check_ip_method.py`](04-Python-OOP/Day-03/04_static%20Variable%20&%20methods/05_@method_check_ip_method.py)

### 6. Resilient Scripting & Exception Handling
- Implementing defensive `try-except-finally` blocks to catch specific runtime errors (`TypeError`, `ZeroDivisionError`, OS permission errors).
- Ensuring automated jobs handle unexpected input without terminating prematurely.
- Script reference: [`04_try_except.py`](02-TrainWithShubham-Python/Day-05/04_try_except.py)

---

## Practical Projects Directory

A quick index of the key practical tools and exercises built across the repository:

| Project / Tool | Location | Focus Area |
|---|---|---|
| **System Health Auditor** | [03_system_health.py](02-TrainWithShubham-Python/Day-05/03_system_health.py) | CPU/RAM/Disk metrics audit & health report |
| **FastAPI Metrics Endpoint** | [01_api.py](02-TrainWithShubham-Python/Day-03/fastapi/01_api.py) | Microservice returning JSON system telemetry |
| **Automated Directory Backup** | [backup.py](03-TrainWithShubham-Python-for-DevOps/Day_02/backup_usingpy/backup.py) | Timestamped file compression and archiving |
| **AWS S3 File Uploader** | [01_s3_upload.py](02-TrainWithShubham-Python/Day-05/01_s3_upload.py) | Programmatic upload to Amazon S3 bucket |
| **AWS S3 Bucket Auditor** | [s3_buckets_names.py](03-TrainWithShubham-Python-for-DevOps/Day-03/boto3_practice/s3_buckets_names.py) | Cloud resource discovery with Boto3 |
| **DevOps Server Manager (OOP)** | [05_devops_serverPractice.py](04-Python-OOP/Day-02/05_devops_serverPractice.py) | Object-oriented server state & deployment management |
| **Modular System Info Collector** | [systemdetails](02-TrainWithShubham-Python/Day-02/projects/systemdetails/) | Decoupled telemetry collection module |
| **Live CPU & RAM Alerting** | [real_cpu_check.py](02-TrainWithShubham-Python/Day-02/projects/real_cpu_check.py) | Real-time threshold breach detection |
| **REST API Consumer** | [02_call_api.py](02-TrainWithShubham-Python/Day-06/02_call_api.py) | External API consumption with timeout & status check |
| **Number Guessing Game** | [23_mini-project-guessing_number.py](01-Apna-College-Python/Day-04/23_mini-project-guessing_number.py) | Interactive CLI logic with loops and random states |

---

## Repository Structure

```text
python-for-devops/
│
├── 01-Apna-College-Python/              # Step 01: Core Python fundamentals
│   ├── Day-01/                         # Printing, variables, types, operators
│   ├── Day-02/                         # Conditions, comparison, range
│   ├── Day-03/                         # Loops, lists, tuples, sets, dictionaries
│   ├── Day-04/                         # Functions, modules, mini-projects
│   └── README.md                       # Detailed course documentation
│
├── 02-TrainWithShubham-Python/          # Step 02: Systems Python & early DevOps
│   ├── Day-01/                         # Basic output & variables
│   ├── Day-02/                         # Collections, conditionals, psutil projects
│   ├── Day-03/                         # FastAPI metrics microservice
│   ├── Day-04/                         # AWS Boto3 bucket discovery
│   ├── Day-05/                         # S3 uploads, system health audit, try-except
│   ├── Day-06/                         # Cloud collections & REST API client
│   └── README.md                       # Detailed course documentation
│
├── 03-TrainWithShubham-Python-for-DevOps/ # Step 03: 4-Hour DevOps workshop
│   ├── Day_01/                         # Syntax refresher & calculator
│   ├── Day_02/                         # OS system commands & automated backup
│   ├── Day-03/                         # Backup archive variations & Boto3 practice
│   └── README.md                       # Detailed course documentation
│
├── 04-Python-OOP/                      # Step 04: Object-Oriented Architecture
│   ├── Day-01/                         # Classes & ATM simulation
│   ├── Day-02/                         # Constructors, self, Server management class
│   ├── Day-03/                         # Encapsulation, static methods, reference passing
│   ├── Day-04/                         # Aggregation, inheritance, polymorphism, super()
│   ├── Day-05/                         # Method overloading & operator overloading
│   └── README.md                       # Detailed course documentation
│
├── 05-Python-for-DevOps-Abhishek/      # Step 05: Real-world enterprise use cases (Upcoming)
│   ├── Day-01/                         # Real-time list handling & exception recovery
│   └── README.md                       # Course roadmap and scope documentation
│
├── .gitignore                          # Git exclusions (env, cache, OS files)
└── README.md                           # Repository overview & learning path
```

---

## How to Use This Repository

If you are exploring this repository or following a similar learning path:

1. **If you are new to Python:** Start with [`01-Apna-College-Python`](01-Apna-College-Python/README.md) to build confidence with variables, syntax, loops, and functions.
2. **If you already know Python basics:** Jump to [`02-TrainWithShubham-Python`](02-TrainWithShubham-Python/README.md) and [`03-TrainWithShubham-Python-for-DevOps`](03-TrainWithShubham-Python-for-DevOps/README.md) to inspect operational scripts for `psutil`, `shutil` backups, and `boto3`.
3. **If you want to write structured tools:** Study [`04-Python-OOP`](04-Python-OOP/README.md) to see how servers, deployments, and infrastructure components can be modeled as reusable classes.
4. **To run the scripts locally:**
   ```bash
   # Clone the repository
   git clone https://github.com/FazalHamzaKhan12/python-for-devops.git
   cd python-for-devops

   # Create and activate a virtual environment
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate

   # Install required third-party libraries
   pip install psutil requests fastapi uvicorn boto3
   ```

---

## Learning Philosophy

> **Learn → Code → Break things → Fix them → Build small tools → Apply to DevOps**

This repository is intentionally kept as an authentic learning log. Exercises reflect real progression from simple beginner scripts to multi-file modules, error handling, and cloud integrations.

---

## Future Goals

The journey continues beyond basic scripting toward full-stack DevOps automation:

- [ ] **Linux & Docker Automation:** Managing Docker containers and inspecting logs via the `docker-py` SDK.
- [ ] **Advanced AWS Automation:** Automating EC2 lifecycle management, Lambda event triggers, and IAM policy audits with Boto3.
- [ ] **CI/CD Integration:** Building custom Python CLI tools invoked within GitHub Actions pipelines.
- [ ] **Kubernetes Client:** Interacting with Kubernetes clusters programmatically using the official `kubernetes` Python client.
- [ ] **Log Parsing & Incident Triage:** Real-time log scraping and alerting for automated incident response.

---

## Author

**Fazal Hamza Khan**  
Aspiring DevOps & Cloud Engineer  
*Bridging software engineering logic with scalable cloud infrastructure.*