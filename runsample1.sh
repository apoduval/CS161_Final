#FILE ATTEMPTING TO RECREATE THE RUN SAMPLE FILE TO TEST 


#!/usr/bin/env bash
#PROJ_PATH=. 
#/usr/class/cs161/project

if [ $# -ne 1 ]; then
  echo "Usage: ./runsample.sh PYTHONSOURCEFILE"
  exit
fi

echo "Running python file $1. Timing results:"
time python $1 < ./sample.in | python ./judge.py ./sample.out
