Big Zip

## Problem

Unzip this archive and find the flag

* [Download zip file](https://artifacts.picoctf.net/c/554/big-zip-files.zip)

## Solution

Zip downloaded is even bigger than zip downloaded from CTF "First Find."  The challange doesn't give us the name of the txt file as previously.  But like all flags in picoCTF, we know the starting characters are picoCTF=.  Using `grep "picoCTF=" ./big-zip-files -R`.  The flag is found in a unspecified file.  The flag is picoCTF{gr3p_15_m4g1c_ef8790dc} 
