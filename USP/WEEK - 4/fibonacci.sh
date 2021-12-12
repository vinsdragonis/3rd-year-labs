#!/bin/bash

echo -e "Enter n: \c"
read n

first=0
second=1

if ((n >= 1))
then 
	printf "%d " $first
fi
if ((n >= 2))
then
	printf "%d " $second
fi

((n = n - 2))
while ((n > 0))
do
	((third = first + second))
	printf "%d " $third
	((first = second))
	((second = third))
	((n--))
done

echo # add a newline
