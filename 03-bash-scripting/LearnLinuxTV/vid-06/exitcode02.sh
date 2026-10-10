#!/bin/bash


dir=/notexist

if [ -d $dir ]
then
	echo "The direcory $dir exists."
else
	echo "The direcotoy $dir doesn't exist."
fi

echo "the exit code for this script is $?"
