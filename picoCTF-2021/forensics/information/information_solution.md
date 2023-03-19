# Information
## Problem
Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Solution
Download the command line tool exiftool with `sudo apt install libimage-exiftool-perl`

With exiftool, scan the picture.  The licenese will look weird.  That text is modified with
Base64.  I didn't know it was base64 without looking so I guess get into the habbit of assuming
things arn't always in plain text.

To decrypt the message use command `echo -n 'cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9' | base64 --decode`
