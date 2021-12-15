# Python Wrangling
## Problem
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?

## Links
* [this Python script](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/ende.py)
* [this password](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/pw.txt)
* [the flag](https://mercury.picoctf.net/static/0bf545252b5120845e3b568b9ad0277e/flag.txt.en)

## Solution
The script, encrypted message, and password are given.  Using redirections in Linux the solution 
```bash
python ende.py -d flag.txt.en < pw.txt
```

Will result with the flag being shown on the terminal
