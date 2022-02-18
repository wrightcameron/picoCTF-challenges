# Nice netcat
## Problem
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

## Solution
The command nc mercury.picoctf.net 22342 returns a bunch of numbers, one on each line.

If I use the command `man ascii` I can quickly see that the first 4 characters spell out pico.  This means that its an ASCII message.
