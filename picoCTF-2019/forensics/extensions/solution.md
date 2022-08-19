# extensions

## Problem

This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Links

* [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)

## Notes

Using the vim command, the file is a bunch of binary with some text but doing a quick find I couldn't find the flag starting with the text "picoCTF".  Using the command `file flag.txt`, the file is reconized as a png file.  Using the image viewer `eog flag.txt` the image that opens up a png image that shows the flag.  The flag picoCTF{now_you_know_about_extensions}

## Solution

flag.txt file that is downloaded is a png file, found with `file flag.txt`.  Opening up the file with `eog flag.txt` shows the flag clearly.  The flag is picoCTF{now_you_know_about_extensions}

