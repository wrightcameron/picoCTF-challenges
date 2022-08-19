# plumbing
## Problem
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `jupiter.challenges.picoctf.org 7480.`

## Notes
Original hints for the challenge recommend using pipes, I wonder if I can use pipes at all or tell wget not to keep retrying to make getting the file cleaner.

I can use the wget -t 1 flag to limit to retries to just 1.

The hint on using pipes is alluding to using netcat to solve this challenge. wget got lucky, but with net cat I can run command `nc jupiter.challenges.picoctf.org 7480 > file` and the file will contain the same results as with wget.

## Solution
Used the command `wget jupiter.challenges.picoctf.org:7480` and an index file was created.  The wget command wanted to keep retrying to connect to this site and port and failing but the index.html file that is created each time contained the flag in it.

picoCTF{digital_plumb3r_06e9d954}
