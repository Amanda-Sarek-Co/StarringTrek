#!/usr/bin/env bash

# don't even ask
pass() {
	echo PASS
}

# line break function, for formatting
lb () {
	for lines in $1
	do
		echo ""
	done
}


check_for_dir() {
	if [ -d "./env" ]
	then
		echo the venv directory is present, make sure that its active before continuing
		lb 1 
		read -p "Press Enter to Continue. . ."
		lb 1 
	else
		python3 -m venv ./env 
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

	if ! pip freeze == cat requirements.txt
	then	
		pip install -r ./requirements.txt 
	fi
}

alias pass="echo PASS"

lb 2 
check_for_dir

lb 2 
python_ver_check
pass

lb 2 
check_pip_packages
pass

lb 2 
