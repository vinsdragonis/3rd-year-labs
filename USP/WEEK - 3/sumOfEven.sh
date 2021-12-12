#!/bin/bash

if [ $# -ne 1 ]
then
   echo 'Enter range'
   exit 128
fi

sum=0

for ((i=0;i<=$1;i++))
do
   if ((i%2==0))
   then
      sum=$((i+sum))
   fi
done

echo "Sum = $sum"
