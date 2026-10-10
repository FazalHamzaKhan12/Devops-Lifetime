# Disk Usage Monitor

A beginner-friendly Bash scripting project that monitors Linux disk usage and displays a status based on usage percentage.

## Features

- Displays the current date and time.
- Shows total, used, and available disk space.
- Calculates disk usage percentage.
- Displays `NORMAL`, `WARNING`, or `CRITICAL` status.

## Requirements

- Linux
- Bash
- `df`, `awk`, and `sed`

## Usage

```bash
chmod +x disk_usage_monitor.sh
./disk_usage_monitor.sh
```

## Disk Usage Thresholds

| Usage | Status |
|---|---|
| Below 80% | NORMAL |
| 80%–89% | WARNING |
| 90% or above | CRITICAL |

## Concepts Practiced

Bash variables, command substitution, `if/elif/else`, comparison operators, pipes, `awk`, `sed`, and Linux disk monitoring.

## Purpose

Created as a hands-on project to practice Bash scripting and learn basic server monitoring for DevOps.
