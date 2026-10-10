#!/bin/bash

while [ -f ~/testfile  ]
do
	echo "As of current $(date), The test file exists."
	sleep 2
done

echo "The file no longer exists. Exiting. as of $(date)"
