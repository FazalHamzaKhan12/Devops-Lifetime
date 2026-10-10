#!/bin/bash

releasefile=/etc/os-release

if grep -q "Arch" $releasefile 
then
	sudo pacman -Syu
fi

if grep -q "Ubuntu" $releasefile
then
	sudo apt update
	sudo apt dist-upgrade
fi
