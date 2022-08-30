# c0rrupt

## Problem

We found this [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery). Recover the flag.

## Links

* [file](https://jupiter.challenges.picoctf.org/static/ab30fcb7d47364b4190a7d3d40edb551/mystery)

## Notes

The file is corrupted and using commands like `vim`, `objdump`, & `hexdump` are not helping out in finding what is wrong with the file.  The first hint of this challange though mentions that the file needs to have its file header changed.  For this we will need two tools.

* [List of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
* [How do I change file headers from the command line?](https://askubuntu.com/questions/1034267/how-do-i-change-file-headers-from-the-command-line)

Using `xxd` for modifying bytes in a binary file is very useful.  Without any arguments too the command gives us the hex value with ascii convertion to the command line.

```bash
$ xxd mystery | head
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
```

Looking at the top row, it does appear that this file looks like corrupted PNG file, the magic numbers at the top are very close to what PNG uses. `89 50 4E 47 0D 0A 1A 0A`.  To change this file so its reconized as a PNG file xxd can be used as, 

```bash
xxd -r -p -o 0 <(echo 8950 4E47 0D0A 1A0A) mystery
```

With that command executed, doing `file mystery` shows the file is still not reconized as a PNG, other parts of the file are corrupted.  
## Solution

Answer
