# strings it
## Problem
Can you find the flag in *file* without running it?

## Links
* [file](https://jupiter.challenges.picoctf.org/static/5bd86036f013ac3b9c958499adf3e2e2/strings)

## Notes
Found the flag in the file, but with vim.  Come back to this challenge and see if I can use strace,
objdump, or string to get the flag out.  Might be more elegant ways.

## Solution
Vim the file and search for the first text picoCTF, the key was found complete in text in the file.
picoCTF{5tRIng5_1T_827aee91}
