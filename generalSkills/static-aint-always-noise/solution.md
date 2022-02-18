# Static Ain't Always Noise
## Problem
Can you look at the data in this binary: **static**? This **BASH script** might help!

## Links
* [static](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/static)
* [BASH script](https://mercury.picoctf.net/static/ec4dbd8898ade34e1d60d5b70c1b8c8c/ltdis.sh)

## Notes
The ltdis.sh script is simple, all it does is run the command `objdump -Dj .text $1 > $1.ltdis.x86_64.txt` on the binary file static.  Checks if a file was created, and if so runs the command `strings -a -t x $1 > $1.ltdis.strings.txt`.

The objdump file is for viewing object files, like binaries.  The -D flag tells the command to "Like -d, but disassemble the contents of all sections, not just those expected to contain instructions."  The -j flag "Display information only for section name." and so our command is only getting disassembly information from the .text section.

The strings command is printing the printable characters in the file created by objdump.  The -a flag tells it to scan the entire document.  The -t flag is a radix flag, its assuming that the sequence in the file is hex.

Need further tutorials on both objdump and strings to get better understanding.

* https://www.howtogeek.com/427805/how-to-use-the-strings-command-on-linux/

## Solution
Running the bash script yields two files. The static.ltdis.strings.txt contains the flag in the file.  This problem was easy, but the method of how the flag was found is more important than the challenge.  In the future there will be similar challenges but they won't tell you to use the objdump command or to use the strings command.

picoCTF{d15a5m_t34s3r_98d35619}