#Wave a flag
## Problem
Can you invoke help flags for a tool or binary? *This program* has extraordinarily 
helpful information...

## Links
* [This program](https://mercury.picoctf.net/static/b28b6021d6040b086c2226ebeb913bc2/warm)

## Solution
This is solved by just running the binary, but running binaries is dangerous.

Here are notes on analysing a binary through Linux commands
[10 ways to analyze binary files on Linux](https://opensource.com/article/20/4/linux-binary-analysis)

Using commands from this article, the binary itself doesn't appear to complex, those
additional work can be done to try to decompile it.  The script is C with debug information included.
