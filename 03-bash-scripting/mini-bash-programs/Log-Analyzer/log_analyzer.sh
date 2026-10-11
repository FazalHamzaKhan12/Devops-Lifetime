#!/bin/bash


log_name=$1




if [ $# -ne 1 ]
then
	echo "Please Provide only 1 Arugment..."
	exit 1
fi


echo "==============================="
echo "       LOG FILE ANALYZER       "
echo "==============================="


if [ -f "$log_name" ]  && [ -r "$log_name" ]
then
	echo "File Exist and its Readable"
elif [ -f "$log_name" ]
then
	echo "File Exsit but not Readable"
else
	echo "File Doesn't exist"
	exit 1
fi

echo

error_count=$(grep -c "ERROR" "$log_name")
warning_count=$(grep -c "WARNING" "$log_name")
info_count=$(grep -c "INFO" "$log_name")


echo "ERROR count: "$error_count"" 
echo "WARNING count: "$warning_count"" 
echo "INFO count: "$info_count"" 

total_count=$(( error_count + warning_count + info_count ))
echo "Total : $total_count"


echo "Analysis completed"

