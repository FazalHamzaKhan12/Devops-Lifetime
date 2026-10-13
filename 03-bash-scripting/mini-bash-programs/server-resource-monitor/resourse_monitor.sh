#!/bin/bash

echo "=============================="
echo "    SERVER RESOURCE MONITOR   "
echo "=============================="

date_time=$(date +"%Y-%m-%d %H:%M:%S")

mkdir -p logs
echo

echo "Date: $date_time"

echo

usage_function(){


	echo "CPU Load: $(uptime | awk '{print $(NF-2), $(NF-1), $NF}')"

	memory_usage="$(free | awk '/Mem:/ {printf "Memory Usage: %.2f%%\n", ($3/$2)*100}')"
	echo "$memory_usage"

	memory_only_in_no=$(free | awk '/Mem:/ {printf "%.0f\n", ($3/$2)*100}')	

	disk_usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
	echo "Disk Usage: $disk_usage%"

	echo

	if [ "$disk_usage" -ge 80 ] && [ "$memory_only_in_no" -ge 80 ]
	then
		echo "Warning Disk Usage & Memory Usage is reaches 80%"
	elif [ "$disk_usage" -ge 80 ]
	then
		echo "Warning Disk Usage Reaches 80%"
	elif [ "$memory_only_in_no" -ge 80 ]
	then
		echo "Warning Memory usage reaches 80%"
	else
		echo "Status: SYSTEM HEALTHY"
	fi
}

usage_function

