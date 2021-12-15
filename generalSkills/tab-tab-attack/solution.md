# Tab, Tab, Attack
## Problem
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: *Addadshashanammu.zip*

## Links
* [Addadshashanammu.zip](https://mercury.picoctf.net/static/e38f6a5b69b45d21e33cf7281d8c2531/Addadshashanammu.zip)

## Notes
The zip file contains an archive of the contents, using zip I can view the internal files without zipping. Opening the binary file at the end I can see the flag in text inbetween binary.

TODO: Check if I can use the objdump command from the last challenge to get the flag, just using vim was luck and very brutish.

## Solution
picoCTF{l3v3l_up!_t4k3_4_r35t!_f3553887}