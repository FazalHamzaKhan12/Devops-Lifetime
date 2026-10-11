# Bash Log File Analyzer

A beginner-friendly Bash scripting project that analyzes log files and counts `ERROR`, `WARNING`, and `INFO` messages.

## Features

- Accepts a log file path as a command-line argument.
- Validates the argument count.
- Checks whether the file exists and is readable.
- Counts lines containing `ERROR`, `WARNING`, and `INFO`.
- Displays a summary report.
- Uses exit codes to handle invalid input.

## Requirements

- Linux
- Bash
- `grep`

## Usage

```bash
chmod +x log_analyzer.sh
./log_analyzer.sh app.log
```

Replace `app.log` with the path to your log file.

## Example Output

```text
===============================
       LOG FILE ANALYZER
===============================

File exists and is readable

ERROR count: 3
WARNING count: 6
INFO count: 19

Analysis completed.
```

*Counts above are illustrative; actual results depend on your log file.*

## Concepts Practiced

Bash variables, command-line arguments, file conditions (`-f`, `-r`), command substitution, `grep -c`, arithmetic expansion, and exit codes.

## Purpose

Built as a hands-on project to practice Bash scripting and learn basic log analysis for DevOps.
