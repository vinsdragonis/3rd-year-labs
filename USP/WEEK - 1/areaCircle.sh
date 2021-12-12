#!/bin/sh

echo "Enter the radius "
read r

area=`echo 22/7 \* $r \* $r|bc`
echo "The area of the circle is: $area" 
