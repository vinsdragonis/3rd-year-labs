#!/bin/bash

if [ $# -ne 2 ]
then
   echo 'Enter 2 numbers'
   exit 128
fi

res=`expr $(($1**$2))|bc`

echo "$1 ^ $2 = $res"
