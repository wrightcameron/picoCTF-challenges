# like1000

## Problem

This [.tar file](https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar) got tarred a lot.

## Links

* [.tar file](https://jupiter.challenges.picoctf.org/static/52084b5ad360b25f9af83933114324e0/1000.tar)

## Solution

The tar file is named 1000.tar, and doing `tar -xvf 100.tar` reveals another file named 999.tar and a junk file.  Easiest way to solve this is with a bash script.

```bash
#!/bin/bash
# Loop through file and obtain flag

for ((i=1000; i>=0; i--)); do
    tar -xf $i.tar 
    rm $i.tar
done
```

As expected the flag is at the bottom tar file, it is inside a png file.

Flag is picoCTF{l0t5_0f_TAR5}

