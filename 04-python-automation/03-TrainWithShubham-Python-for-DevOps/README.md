# TrainWithShubham - Python for DevOps (4-Hour Workshop)

A fast-paced workshop focused on real-world DevOps scripting, including OS system commands, automated time-stamped directory backups (`shutil`, `os`, `datetime`), and AWS S3 automation using `boto3`.

## About This Course

- **Course:** Give Me 4 Hours, I Will Make You PRO in Python for DevOps
- **Instructor / Channel:** Shubham Londhe ([TrainWithShubham YouTube Workshop](https://youtu.be/mM6X7wjEtag))
- **Focus:** Practical DevOps automation: OS library interaction, shell commands, automated backup pipelines, and AWS Boto3 SDK scripting.
- **Why It Is Useful:** Bridges the gap between core Python syntax and day-to-day sysadmin/DevOps tasks. It specifically answers the question: *"How do I replace Bash scripts with Python for file handling, backups, and cloud resource management?"*
- **Where It Fits in the DevOps Journey:** Step 03 in the learning journey. Provides immediate hands-on practice in writing automation scripts that interact directly with the operating system and cloud APIs.

## Topics Covered

| Status | Topic | Details |
|---|---|---|
| ✅ | Python Refresher | Variables, user input, simple math operations, list manipulation |
| ✅ | Control Structures & Loops | `for` loops, iteration over lists, conditionals |
| ✅ | OS Library & System Commands | `os.system()` to invoke native shell commands (`systeminfo`) |
| ✅ | File & Archive Automation | `shutil.make_archive()`, `os.path.join()`, `datetime.date.today()` |
| ✅ | Automated Backup Scripting | Building dated backup archives (`.zip` / `.tar.gz`) of directories |
| ✅ | AWS Boto3 SDK Setup | Initializing Boto3 S3 resources and credentials |
| ✅ | Cloud Asset Discovery | Enumerating and filtering S3 buckets programmatically |
| ✅ | Iterative Script Refinement | Multiple practice variations refining backup and Boto3 scripts |

## Practical Examples

| Script / Project | Purpose | Python Concept | Why It Is Useful |
|---|---|---|---|
| [03_import_os_lib.py](Day_02/03_import_os_lib.py) | Invokes host operating system commands | `import os`, `os.system()` | Interacting with shell commands and host environments |
| [backup.py](Day_02/backup_usingpy/backup.py) | Creates a dated archive (`.zip`/`.tar.gz`) of a folder | `shutil`, `datetime`, `os.path` | Automated backup cron jobs for logs, configs, and application data |
| [backup_practice_4.py](Day-03/backup_archive/backup_practice_4.py) | Refined backup script with custom source/destination | File system paths, functions, archiving | Safe, repeatable directory archiving routines |
| [s3_buckets_names.py](Day-03/boto3_practice/s3_buckets_names.py) | Connects to AWS S3 and prints all bucket names | `boto3.resource("s3")`, loops | Automated cloud asset discovery and compliance auditing |
| [s3_buckets_names_practice_4.py](Day-03/boto3_practice/s3_buckets_names_practice_4.py) | Encapsulated function for querying S3 buckets | Modular functions, SDK parameters | Integrating S3 inventory checks into larger workflows |

## Python Concepts Learned

- **System Command Execution:** Calling external OS binaries via `os.system()`.
- **Filesystem & Archiving Utilities:** Using the Python standard library's `shutil` module to compress directories into `zip` or `gztar` formats without external zip binaries.
- **Dynamic File Naming:** Utilizing `datetime.date.today()` or timestamp formatting to generate unique, dated backup filenames (e.g., `backup_2026-09-10.tar.gz`).
- **AWS Cloud SDK (`boto3`):** Initializing AWS service resources (`boto3.resource('s3')`) and iterating across cloud collections.
- **Iterative Refinement:** Practicing concepts multiple times across variations (`backup_practice_1` through `backup_practice_4`) to build muscle memory.

## DevOps Relevance

- **Log & Config Backups:** Scheduled backups are a standard operational task. Python scripts using `shutil` and `datetime` provide cross-platform backup capabilities that work on both Linux and Windows.
- **Disaster Recovery Pipelines:** Combining local directory compression with S3 uploads creates a reliable offsite disaster recovery pipeline.
- **Cloud Inventory Automation:** Querying S3 buckets via Boto3 is the foundation for cost optimization, bucket policy auditing, and automated cleanup scripts.

## Learning Notes

- Hardcoded paths (e.g., `C:/Users/...`) can cause scripts to fail when executed on different machines or inside Docker containers. In production, use `os.path.abspath()`, relative paths, or environment variables (`os.environ.get()`).
- `os.system()` runs commands in a subshell and only returns the exit status code. For capturing standard output or piping data, Python's `subprocess.run()` is preferred in advanced workflows.
- `boto3` requires valid AWS credentials (`~/.aws/credentials` or environment variables) to authenticate with AWS APIs.

## Projects / Exercises

### Day 01 — Fundamentals Refresher
- [01_variables.py](Day_01/01_variables.py)
- [02_input.py](Day_01/02_input.py)
- [03_basic_calculator.py](Day_01/03_basic_calculator.py)
- [04_conditional.py](Day_01/04_conditional.py)
- [05_list.py](Day_01/05_list.py)
- [06_loops.py](Day_01/06_loops.py)

### Day 02 — OS Integration & Automated Backup
- [01_for_loops.py](Day_02/01_for_loops.py)
- [03_import_os_lib.py](Day_02/03_import_os_lib.py)
- [04_function.py](Day_02/04_function.py)
- [backup.py](Day_02/backup_usingpy/backup.py)

### Day 03 — Backup Archive Refinement & AWS Boto3
- **Automated Backup Iterations:**
  - [backup_practice.py](Day-03/backup_archive/backup_practice.py)
  - [backup_practice_2.py](Day-03/backup_archive/backup_practice_2.py)
  - [backup_practice_3.py](Day-03/backup_archive/backup_practice_3.py)
  - [backup_practice_4.py](Day-03/backup_archive/backup_practice_4.py)
- **AWS Boto3 S3 Automation:**
  - [s3_buckets_names.py](Day-03/boto3_practice/s3_buckets_names.py)
  - [s3_buckets_names_practice.py](Day-03/boto3_practice/s3_buckets_names_practice.py)
  - [s3_buckets_names_practice_2.py](Day-03/boto3_practice/s3_buckets_names_practice_2.py)
  - [s3_buckets_names_practice_3.py](Day-03/boto3_practice/s3_buckets_names_practice_3.py)
  - [s3_buckets_names_practice_4.py](Day-03/boto3_practice/s3_buckets_names_practice_4.py)

## What I Learned

Built operational scripts for automated backups using `shutil` and timestamped naming, executed OS-level commands via `os.system()`, and connected to AWS cloud infrastructure via Boto3 to discover S3 resources.

## Next Step

Move to [04-Python-OOP](../04-Python-OOP/README.md) to understand Object-Oriented Programming in Python and learn how to model infrastructure components (servers, clusters, deployments) as structured classes.
