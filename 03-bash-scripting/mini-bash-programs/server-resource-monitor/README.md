# Server Resource Monitor

A beginner-friendly Bash scripting project that monitors basic Linux system resources, including CPU load, memory usage, and disk usage. It displays warnings when memory or disk usage reaches 80% or higher.

## Features

- **CPU Load Monitoring:** Displays the system load averages.
- **Memory Monitoring:** Calculates memory usage as a percentage.
- **Disk Monitoring:** Checks disk usage for the root filesystem (`/`).
- **Threshold Alerts:** Displays warnings when memory or disk usage reaches 80%.
- **System Status:** Reports whether the system is healthy or requires attention.
- **Log Directory:** Creates a `logs` directory for storing monitoring reports when used with output redirection.

## Project Structure

```text
server-resource-monitor/
├── resource_monitor.sh
├── README.md
└── logs/
```

## Requirements

- Linux operating system
- Bash
- `awk`
- `df`
- `free`
- `uptime`
- `sed`

These commands are commonly available on Linux systems.

## How to Run

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Enter the project directory

```bash
cd server-resource-monitor
```

### 3. Make the script executable

```bash
chmod +x resource_monitor.sh
```

### 4. Run the monitor

```bash
./resource_monitor.sh
```

## Example Output

```text
==============================
    SERVER RESOURCE MONITOR
==============================

Date: 2026-10-13 15:30:00

CPU Load: 0.45, 0.38, 0.30
Memory Usage: 65.25%
Disk Usage: 42%

Status: SYSTEM HEALTHY
```

*The values above are examples. Actual results depend on your system.*

## Alert Conditions

| Condition | Result |
|---|---|
| Disk usage is 80% or higher and memory usage is 80% or higher | Warns about both |
| Disk usage is 80% or higher | Warns about disk usage |
| Memory usage is 80% or higher | Warns about memory usage |
| Both are below 80% | Reports system healthy |

## Save Reports to a Log File

To display the output and append it to a log file, run:

```bash
mkdir -p logs
./resource_monitor.sh | tee -a logs/resource_monitor.log
```

To view saved reports:

```bash
cat logs/resource_monitor.log
```

The `tee -a` command appends new output to the file rather than replacing previous reports.

## Concepts Practiced

- Bash scripting
- Variables and command substitution
- Functions
- Conditional statements (`if`, `elif`, `else`)
- Numeric comparisons (`-ge`)
- Linux system monitoring commands
- Text processing with `awk` and `sed`
- Pipes and output logging

## Real-World Use Case

DevOps engineers monitor server resources to identify high memory consumption, increasing disk usage, and possible capacity problems. This project demonstrates the basic checks that can be used as part of a larger monitoring script.

## Future Improvements

- Save reports automatically from within the script.
- Add CPU usage percentage monitoring.
- Allow custom warning thresholds.
- Add error handling for failed commands.
- Schedule monitoring with `cron`.

## Author

Created as part of my hands-on DevOps and Bash scripting learning journey.
