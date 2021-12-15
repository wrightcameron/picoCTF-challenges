# Magikarp Ground Mission
## Problem
Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `481e7b14`

## Notes
Following the text directions leads to completing the challenge.  But another way to solve or find all the files is to use the find command.  The first 2 flag files have flag in the name, so assuming the third one does as well.  The find command will work, `find / -name "*flag*" -print 2> /dev/null`.  Using this find command you can scan all parts of the system for the flags.

## Solution
The challenge is to ssh onto a docker container running ubuntu.  In this server are parts of the flag scattered between the launding dir, root directory, and the home of the user.  Each of these dir have a part of the flag and a text file saying where the next one is.

