#/bin/bash


echo "==========================="
echo "    LOG BACKUP SCRIPT"
echo "==========================="

dir=$1

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

    local date_time=$(date +"%Y-%m-%d_%H-%M-%S")

    echo "Creating Backup...."
    sleep 0.6

    tar -czf "logs_${date_time}_file.tar.gz" "$dir"
}



backup_checker
create_backup
