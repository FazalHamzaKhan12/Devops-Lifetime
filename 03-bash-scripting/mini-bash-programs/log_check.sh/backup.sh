#!/bin/bash
echo

echo "==========================="
echo "    LOG BACKUP SCRIPT"
echo "==========================="

dir=$1


if [ ! $# -eq 1  ]
then	echo "Add arugument First to continue"
	exit 1
fi


backup_checker(){




        if [ -d "$dir" ]
        then
                echo "Log directory: $dir"
                echo "Log files    : $(find "$dir" -type f -name "*.log" | wc -l )"
        else
                echo "Not Exist"
                exit 1
        fi

}


create_backup(){
	
	echo 
	local date_time=$(date +"%Y-%m-%d_%H-%M-%S")
	
	if [ ! -d "$dir/backup" ]
	then
		echo "Creating backupFolder..."
		sleep 0.6
		mkdir -p "$dir"/backup
		echo "backup created successfully"
	else
		echo "SIR! The folder is already exist" > /dev/null
	fi
    
	echo "Backup directory Location: "$dir/backup" "
	echo "Creating the Archive...."
	echo 


	echo "Adding the zip file"
	
	tar -czf "$dir/backup/logs_${date_time}_file.tar.gz" \
    $(find "$dir" -maxdepth 1 -type f -name "*.log")

	echo "Backup size: $(du -h "$dir/backup/logs_${date_time}_file.tar.gz" | cut -f1)"
}



backup_checker
create_backup
