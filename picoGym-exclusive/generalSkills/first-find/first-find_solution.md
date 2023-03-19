# First Find

## Problem

Unzip this archive and find the file named 'uber-secret.txt'

* [Download zip file](https://artifacts.picoctf.net/c/551/files.zip)

## Notes

This challange can be done quickly by using the command line with the following commands to quickly find the flag.

* `unzip`
* `find` or `tree -a`
* `less` or `cat`

## Solution

Downloading the zip file, and running command `unzip files.zip` shows multiple directories and files containing what looks likes stories written by Charles Dickens that are in the public domain.  First thing done is run `find . -name uber-secret.txt`.  This shows that the file does exists and is found nested deep in this unzipped directoy `./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt`.  The flag is found in text file.  The flag is picoCTF{f1nd_15_f457_ab443fd1}.

