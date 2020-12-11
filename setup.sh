#!/usr/bin/env bash
user=$1

# Some helper functions
pass() {
	echo PASS
}

lb () {
	for lines in $1
	do
		echo ""
	done
}

# Development Environment functions
check_for_dir() {
	if [ -d "./env" ]
	then
		echo the venv directory is present, make sure that its active before continuing
		lb 1 
		read -p "Press Enter to Continue. . ."
		lb 1 
	else
		echo no venv detected, creating one now 
		python3 -m venv ./env 
		echo venv created, activate the script at /env/bin/activate before running this script again
	fi
}

python_ver_check () {
	echo checking for the correct version of Python . . .
	if ! python --version | grep "3.6" 
	then	
		echo Make sure the venv is using Python version 3.6.x	
		exit
	fi
}

check_pip_packages () {
	echo making sure your python packages are up to date . . .

	pip install -r ./requirements.txt 
}

alias pass="echo PASS"

lb 2 
check_for_dir

lb 2 
python_ver_check
pass

lb 2 
check_pip_packages

lb 2 

SETUP COMPLETE

code ./
