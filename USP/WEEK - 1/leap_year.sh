#!/bin/sh

echo -n 'Enter year: '
read y

if [ $((y % 4)) -eq 0 ]
then
   if [ $((y % 400)) -ne 0 -a $((y % 100)) -eq 0 ]
   then
      echo 'Not leap year'
   else
      echo 'Leap year'
   fi
fi
