#!/bin/bash



server_info(){


	local host=$(hostname)
	local who=$(whoami)
	local date=$(date)
	local uptime=$(uptime -p)

	echo "==================================="
	echo "        SERVER HEALTH CHECK        "
	echo "==================================="
	
	echo
	echo "Hostname: $host"
	echo "Username: $who"
	echo "Date: $date"
	echo "Uptime: $uptime"
	echo

}


disk_usage(){
	echo "Disk Usage"
	local disk_num=$(df -h / | awk 'NR==2 {print $5}' | tr -d '%' )
	echo "Disk Usage: $(df -h / | awk 'NR==2 {print $3}')"
	echo "Root filesystem: ${disk_num}%"
	
	if [ "$disk_num" -ge 80 ]
	then
		echo "Warning: Disk usage is high!"
	else
		echo "Disk usage is OKEY"
	fi
}

memory_usage(){

	echo "Memoery Usage"
	echo "Total Memory: $(free -h | awk '/Mem:/ {printf $2}')"
	echo "Memory Usage: $(free -h | awk '/Mem:/ {print $3}')"
	echo "Memory Free: $(free -h | awk '/Mem:/ {print $4}')"
	echo
}


check_service(){

	
	local services=("ssh" "docker")
	echo "Service Status:" 
	for service in ${services[@]}
	do

		if systemctl is-active --quiet "$service"
		then
			echo "$service : IS-RUNNING"
		else
			echo "$service" : NOT RUNNING
		fi
	done
	echo 
}

check_commands(){
	echo "Command Availabilty"

	commadss=("bash" "curl" "git" "docker" "python" "fake-command")

	for comand in ${commadss[@]}
	do
		
		if command -v "$comand" > /dev/null  
		then
			echo "$comand : INSTALLED"
		else
			echo "$comand : NOT INSTALLED"
		fi

	done
	

}



server_info
disk_usage
memory_usage
check_service
check_commands


failed=0

if [ $failed == 0  ]
then
	echo "Healthy"
	exit 0
else
	echo "Warning"
	exit 1
fi
