# Backup & Retention Manager

A beginner-friendly Bash scripting project that automates directory backups, reports backup file sizes, and manages old backups through a retention policy.

## Features

- **Source Validation:** Checks whether the source directory exists.
- **Destination Handling:** Checks the backup destination and creates it when needed.
- **Automated Backups:** Creates compressed `.tar.gz` archives using `tar`.
- **Timestamped Filenames:** Adds the date and time to each backup filename.
- **Backup Size Reporting:** Displays the size of the generated archive.
- **Retention Policy:** Keeps the latest 3 backups and deletes older backup archives.
- **Error Handling:** Reports errors when backup creation fails.

## Project Structure

```text
Backup-Manager/
├── backup_manager.sh
├── source/
│   ├── app.conf
│   ├── app.log
│   └── readme.txt
└── backups/
    ├── backup_2026-10-12_10-30-00.tar.gz
    ├── backup_2026-10-12_10-32-00.tar.gz
    └── backup_2026-10-12_10-36-08.tar.gz
```

*The backup filenames above are examples.*

## Requirements

- Linux
- Bash
- `tar`
- `gzip`
- `du`
- Standard command-line utilities, including `ls`, `cut`, `tail`, and `wc`

## Usage

### 1. Open the project directory

```bash
cd Backup-Manager
```

### 2. Make the script executable

```bash
chmod +x backup_manager.sh
```

### 3. Run the backup script

```bash
./backup_manager.sh ./source ./backups
```

The script accepts two arguments:

- `source`: The directory you want to back up.
- `destination`: The directory where backup archives are stored.

### 4. Check your backups

```bash
ls -lh ./backups
```

## Example Output

```text
=================================
          BACKUP MANAGER
=================================

Source: ./source
Destination: ./backups

Creating Backup...
Backup file Created: ./backups/backup_2026-10-12_10-36-08.tar.gz
Size: 4.0K
Backup created successfully

Total Backups: 4
Deleting Old Backups....
Deleting: ./backups/backup_2026-10-12_10-29-21.tar.gz
Retention completed. Keeping latest 3 backups.
```

## How the Retention Policy Works

The script checks how many backup archives exist in the destination directory.

- If there are 3 or fewer backups, it keeps them.
- If there are more than 3 backups, it identifies the older backups.
- It keeps the newest 3 and deletes the older ones.

For example, if the destination contains 5 backups, the script should delete the 2 oldest backups and retain the newest 3.

## Concepts Practiced

- Bash variables and command-line arguments
- Functions
- Conditional statements (`if`, `else`)
- Directory validation (`-d`)
- Exit codes and error handling
- Command substitution (`$(...)`)
- Date and time formatting with `date`
- Archive creation using `tar -czf`
- File size reporting with `du -h`
- Pipes (`|`) and text processing
- Backup retention and automated cleanup

## Real-World Use Case

A DevOps engineer may need to back up application configuration files, logs, or project data regularly. Keeping every backup forever consumes disk space.

A retention policy solves this problem by preserving recent backups while removing older ones automatically.

This project demonstrates the basic logic behind that process. It is a learning project, not yet a production-ready backup system.

## Future Improvements

- Add logging to a dedicated log file.
- Support custom retention counts instead of a fixed limit of 3.
- Add a dry-run mode to preview which backups would be deleted.
- Improve handling of unusual filenames and empty backup directories.
- Add automated scheduling using `cron`.
- Test restoration from a generated backup archive.

## Author

Created as part of my hands-on DevOps and Bash scripting learning journey.
