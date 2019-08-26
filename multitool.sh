#!/bin/bash

if [ "$#" -ge "1" ]; then
	
	if [ "$1" == "IP" ]; then
	
		ifconfig | pcregrep -M -o '^[^\t:]+:([^\n]|\n\t)*status: active' |pcregrep -M -o '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][^255][0-9]{1,2}'
	
	elif [ "$1" == "interface" ]; then
	
		ifconfig | pcregrep -M -o '^[^\t:]+:([^\n]|\n\t)*status: active' |pcregrep -M -o '^[a-zA-Z0-9]{3,7}'

	elif [ "$1" ==  "netmask" ]; then

		ifconfig | pcregrep -M -o '^[^\t:]+:([^\n]|\n\t)*status: active'|pcregrep -M -o '0x[0-9a-f]{8}'

	elif [ "$1" == "nmap" ] && [ "$#" -gt "1" ]; then
		
		nmap -sP $2 |pcregrep -M -o "[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}"

	elif [[ "$1" == "router" ]]; then

		route -n get default |pcregrep -M -o "[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}" 

	else
	
		echo "Error"

	fi

else

	echo "Error"

fi
