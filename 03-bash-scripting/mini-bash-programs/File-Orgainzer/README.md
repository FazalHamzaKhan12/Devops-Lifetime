# Bash File Organizer

A simple Bash scripting project that automatically organizes files into folders based on their file extensions.

## Features

- Accepts a directory path as an argument.
- Creates `logs/`, `text/`, and `configs/` folders.
- Counts `.log`, `.txt`, and `.conf` files.
- Moves files into their respective folders.
- Uses `find` to search for files.
- Supports repeated execution without reprocessing files inside the destination folders.

## Requirements

- Linux
- Bash
- GNU `find` and `mv`

## Usage

```bash
chmod +x file_organizer.sh
./file_organizer.sh ~/organizer_test
```

Replace `~/organizer_test` with the directory you want to organize.

## Example

**Before:**
```text
organizer_test/
├── app.log
├── notes.txt
└── nginx.conf
```

**After:**
```text
organizer_test/
├── logs/
│   └── app.log
├── text/
│   └── notes.txt
└── configs/
    └── nginx.conf
```

## Concepts Practiced

Bash functions, command-line arguments, conditionals, variables, `find`, `mkdir`, `mv`, and file counting with `wc`.

## Purpose

Built as a hands-on project to practice Linux and Bash scripting for DevOps.
