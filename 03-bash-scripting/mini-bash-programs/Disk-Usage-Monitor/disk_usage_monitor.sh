#!/bin/bash

echo
echo "==================================="
echo "         DISK USAGE MONITOR        "
echo "==================================="
echo 

date=$(date +"%Y-%m-%d %H:%M:%S %Z")

echo "Date: "$date""

echo 

echo "Filesystem: $(df -h / | awk '{print $1}' | tail -n 1)"
echo "Total Space: $(df -h / | awk '{print $2}' | tail -n 1 )"
echo "Used Space: $(df -h / | awk '{print $3}' | tail -n 1 )"
echo "Available: $(df -h / | awk '{print $4}' | tail -n 1)"

usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "Usage: "$usage"%"
echo  

if [ "$usage" -ge 90 ]
then
	echo "Status: CRITICAL"
elif [ "$usage" -ge 80 ]
then
	echo "Status: WARNING"
else
	echo "Status: NORMAL"
	echo "Disk usage is within limits"
fi




