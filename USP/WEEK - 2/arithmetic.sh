#!/bin/sh

if [ $# -ne 2 ]
then
	echo 'Enter 2 numbers'
	exit 128
fi

s=`expr $1+$2|bc`
d=`expr $1-$2|bc`
m=`expr $1\*$2|bc`
q=`expr $1/$2|bc`
r=`expr $1%$2|bc`

echo "Sum = $s"
echo "Differnece = $d"
echo "Product = $m"
echo "Quotient = $q"
echo "Remainder = $r"
