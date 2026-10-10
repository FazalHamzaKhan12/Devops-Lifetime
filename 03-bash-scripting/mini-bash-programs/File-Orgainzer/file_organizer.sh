#!/bin/bash


dir=$1

if [ $# -ne 1 ]
then
	echo "Please enter the arugement to Continue..."
	echo "add only 1"
	exit 1
fi


check_directory_exits(){
	
	echo 

	if [ ! -d "$dir" ]
	then
		echo "Creating Directory..."
		sleep 0.9
		mkdir -p "$dir"
	fi
	
	echo "Directory: $dir"
	mkdir -p "$dir/logs" "$dir/text" "$dir/configs"
	echo "Folder created sucessfully."
	


	echo 


	#echo "Logs in NO:   $($dir ls *.log | wc -l)"
	#echo "Text in N0:   $($dir ls *.txt | wc -l)"
	#echo "Configs In NO: "$dir" $(ls *.txt | wc -l )"
}


backup_file(){

	echo "NO 0f .log files: $(find "$dir" -maxdepth 1 -type f -name "*.log" | wc -l)"
        echo "NO 0f .config files: $(find "$dir" -maxdepth 1 -type f -name "*.conf" | wc -l)"
        echo "NO 0f .txt files: $(find "$dir" -maxdepth 1 -type f -name "*.txt" | wc -l)"

   
     	find "$dir" -maxdepth 1 -type f -name "*.log" \
		-exec mv -t "$dir/logs" -- {} +


	find "$dir" -maxdepth 1 -type f -name "*.txt" \
                -exec mv -t "$dir/text" -- {} +

	find "$dir" -maxdepth 1 -type f -name "*.conf" \
                -exec mv -t "$dir/configs" -- {} +

}




check_directory_exits
backup_file
