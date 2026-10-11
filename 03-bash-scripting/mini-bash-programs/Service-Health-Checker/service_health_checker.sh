#!/bin/bash


service1=$1


if [ $# -ne 1 ]
then
	echo "Please Enter one arugument to Conitinue..."
	exit 1
fi


systemctl_checks(){
	
	echo "================================"
	echo "      SERVICE HEALTH CHECK     "
	echo "================================"

	echo "Checking Wheather systemctl is available..."
	sleep 0.5

	local systemctl_checks=$(command -v systemctl)

	if [ "$systemctl_checks" ]
	then	
		echo "systemctl is already installed"
	else
		echo "systemctl is not available"
	fi
	echo
}


service_checker(){

#	local service_active_checks=$(systemctl is-active --quiet  "$service1")
#	local command_checker=$(systemctl status $service1)
	
	if systemctl status "$service1" >/dev/null 2>&1
	then
		if systemctl is-active --quiet "$service1"
       		then
			echo "Service: "$service1""
                	echo "Status: HEALTHY"
			echo "Message: Service is running."
        	else
                	echo "Status: INACTIVE/FAILED"
                	exit 1
        	fi
	else
		echo "The service is not available"
		exit 1
	fi
}


systemctl_checks
service_checker
