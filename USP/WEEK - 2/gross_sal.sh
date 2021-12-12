#!/bin/sh

if [ $# -ne 1 ]
then
	echo 'Enter basic salary'
	exit 128
fi

hra=`expr $1\*20/100|bc`
da=`expr $1\*10/100|bc`

sal=`expr $1+$hra+$da|bc`

echo "Total salary = $sal"
