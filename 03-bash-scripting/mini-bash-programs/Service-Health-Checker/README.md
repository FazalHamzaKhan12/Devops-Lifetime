# Linux Service Health Checker

A beginner-friendly Bash scripting project that checks the status of Linux systemd services and reports whether they are running.

## Features

- Validates command-line arguments.
- Checks whether `systemctl` is available.
- Checks whether a specified service is active.
- Displays `HEALTHY` when a service is running.
- Reports inactive or unavailable services.
- Uses exit codes to handle failed checks.

## Requirements

- Linux with systemd
- Bash
- `systemctl`

## Usage

```bash
chmod +x service_health_checker.sh
./service_health_checker.sh docker
```

Replace `docker` with the name of another service installed on your system.

## Example Output

```text
================================
      SERVICE HEALTH CHECK
================================

Checking whether systemctl is available...
systemctl is already installed

Service: docker
Status: HEALTHY
Message: Service is running.
```

## Concepts Practiced

- Bash variables and functions
- Command-line arguments
- `if/else` conditions
- `command -v`
- `systemctl`
- Command exit statuses
- Output redirection

## Purpose

Built as a hands-on project to practice Linux administration and basic service monitoring for DevOps.
