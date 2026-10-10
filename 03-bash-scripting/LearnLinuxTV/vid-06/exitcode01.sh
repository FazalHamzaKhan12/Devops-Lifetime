#!/bin/bash


package=htop

sudo apt install $package >> package_install_results.log
 
if [ $? -eq 0]
then
	echo "The installation of $package was successfull."
	echo "The new command is availabe here:"
	which $package
else
	echo "$package faild to install." >> package_install_failure.log
fi
