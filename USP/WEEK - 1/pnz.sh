#!/bin/sh

echo "Enter a number "
read n

if [ $((n % 2)) -eq 0 ]
then
   if [ $n -eq 0 ]
   then
      echo 'Zero'
   else
      echo 'Even'   
   fi
else
   echo 'Odd'
fi
