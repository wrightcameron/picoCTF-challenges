#!/usr/bin/bash
# Decrypt a file containing numbers, 1 number be line.  Into ascii
inputfile="mercuryOutput.txt"
while read line
do
	printf "\x$(printf "%x" $line)"
done < $inputfile
