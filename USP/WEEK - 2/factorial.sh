#!/bin/sh

if [ $# -ne 1 ] 
then
	echo 'Insufficient params'
	exit
fi

ans=1
n=1

while [ $n -le $1 ]
do
	ans=`expr $ans \* $n` 
	n=`expr $n + 1`
done

echo "$1! is $ans"
