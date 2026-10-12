#!/bin/bash


source=$1
destination=$2

if [ $# -ne 2 ]
then
	echo "Please Provide only 2 Aruguments" >&2
	echo "Source \ Destination"
	exit 1
fi


echo "================================="
echo "          BACKUP MANAGER         "
echo "================================="
echo

check_source(){

	
	if [ -d "$source" ]
	then
		echo "Source: $source"
	else
		echo "Error: Directory not found or is not a directory: $source " >&2
		exit 1
	fi
	
}


check_destination(){

	
	if [ -d "$destination" ]
	then
		echo "Destination: $destination"
	else
		echo "Creating Backup Directory..."
		sleep 0.4
		mkdir -p backups
	fi
	echo
}

creating_backup(){
	
	echo "Creating Backup..."
	sleep 0.5
		
	local date_time=$(date +"%Y-%m-%d_%H-%M-%S")
	local archive_path="${destination%/}/backup_${date_time}.tar.gz"

	if tar -czf "$archive_path" "$source"
	then
		local size_checker=$(du -h "$archive_path" | cut -f1)
		echo "Backup file Created: $archive_path"
		echo "Size: $size_checker"
		echo "Backup created successfully"
	else
		echo "Error: tar backup creation failed" >&2
		return 1
	fi

	echo 
	echo "dleteing time"
	echo 
	echo 

	local backups_lines
backups_lines=$(ls -1t "$destination"/*.tar.gz 2>/dev/null | wc -l)

echo "Total Backups: $backups_lines"

if [ "$backups_lines" -gt 3 ]
then
    echo "Deleting Old Backups...."

    ls -1t "$destination"/*.tar.gz | tail -n +4 |
    while IFS= read -r old_backup
    do
        echo "Deleting: $old_backup"
        rm -f -- "$old_backup"
    done

    echo "Retention completed. Keeping latest 3 backups."
else
    echo "Retention Policy: Keeping latest 3 backups"
fi

	
}


check_source
check_destination
creating_backup

