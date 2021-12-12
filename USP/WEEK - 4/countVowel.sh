#!/bin/bash

echo -e "Enter string: \c "
read string 

numVowels=`grep -o '[AEIOUaeiou]' <<< $string | wc -l`

echo "No. of vowels: $numVowels"
