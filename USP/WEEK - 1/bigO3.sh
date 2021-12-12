#!/bin/sh

if [ $# -ne 3 ]
then
   echo 'Insufficient params'
   exit 128
fi

if [ $1 -gt $2 -a $1 -gt $3 ]
then
   echo "$1 is the largest"
elif [ $2 -gt $1 -a $2 -gt $3 ]
then
   echo "$2 is the largest"
else
   echo "$3 is the largest"
fi
