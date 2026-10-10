# Log Backup Script

## Description
A beginner Bash scripting project that checks a given directory, counts `.log` files, and creates a compressed backup using `tar`.

## Features
- Accepts a log directory as a command-line argument.
- Checks whether the directory exists.
- Counts `.log` files.
- Creates a backup directory if it doesn't exist.
- Creates a timestamped `.tar.gz` archive.
- Displays the backup size.

## Requirements
- Linux
- Bash
- `find`, `tar`, `date`, and `du`

## Usage

```bash
chmod +x log_backup.sh
./log_backup.sh ~/test_logs
```

## Example
If `~/test_logs` contains several `.log` files, the script creates a compressed backup inside:

```text
~/test_logs/backup/
```

## Bash Concepts Practiced
- Variables and arguments
- Functions
- `if/else` conditions
- `find` and `wc`
- Command substitution
- Directory checks
- `tar` compression
- Exit codes

## Learning Goal
Practice Bash scripting by automating a basic log backup task similar to one used in DevOps operations.

