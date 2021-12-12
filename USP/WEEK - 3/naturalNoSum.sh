#!/bin/bash

if [ $# -ne 1 ]
then
   echo 'Enter range'
   exit 128
fi

sum=0

for ((i=0;i<=$1;i++))
do
   sum=$((i+sum))
done

echo "Sum = $sum"
