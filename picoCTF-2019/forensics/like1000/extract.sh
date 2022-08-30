#!/bin/bash
# Loop through file and obtain flag

for ((i=1000; i>=0; i--)); do
    tar -xf $i.tar 
    rm $i.tar
done
