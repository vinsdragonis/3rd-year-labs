#!/bin/bash

if [ $# -ne 1 ]
then
   echo 'Enter filename'
   exit 128
fi

echo "Line count = " `wc -l $1`
echo "Word count = " `wc -w $1`
echo "Character count = " `wc -m $1`
