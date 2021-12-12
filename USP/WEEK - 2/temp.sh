#!/bin/sh

if [ $# -ne 1 ]
then
	echo 'Enter temperature in Farenheit'
	exit 128
fi

x=`expr $1-32|bc`
c=`expr 5\*$x/9|bc`

echo "$1 degrees in Celsius = $c"
