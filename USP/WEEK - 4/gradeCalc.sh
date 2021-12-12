#!/bin/bash

#CIE marks

echo "Enter CIE marks in all subs"
cie=()

for i in {0..3}
do
  read cie[$i]
done

#SEE marks

echo "Enter SEE marks in all subs"
see=()

for i in {0..3}
do
  read see[$i]
done

# Calculate marks

totalMarks=()

for i in {0..3}
do
  totalMarks[$i]=`expr ${cie[i]}+${see[i]}/2|bc`
done

for i in {0..3}
do
   echo "Grade for subject $i is ="
   
   if [ ${totalMarks[$i]} -ge 90 ]
   then
      echo "S Grade"
   elif [ ${totalMarks[$i]} -ge 80 ]
   then
      echo "A Grade"
   elif [ ${totalMarks[$i]} -ge  70 ]
   then
      echo "B Grade"
   elif [ ${totalMarks[$i]} -ge  60 ]
   then
      echo "C grade"
   elif [ ${totalMarks[$i]} -ge  50 ]
   then
      echo "D grade"
   elif [ ${totalMarks[$i]} -ge  40 ]
   then
      echo "E grade"
   else
      echo "Fail"
   fi
done
