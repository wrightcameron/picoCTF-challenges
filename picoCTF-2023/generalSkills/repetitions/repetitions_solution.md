#  repetitions

## Problem

Can you read files in the root file?

Can you make sense of this file? Download the file [here](https://artifacts.picoctf.net/c/471/enc_flag).

## Notes

The file that is downloaded looks like base64, it also reminds me of ssl public certs with the == at the very end. A quick use of the `file` command shows that the file is just plain ASCII.  The easiest way to solve this problem is to use the site [CyberChef](https://cyberchef.org/) to help solve this encoded file.

Tried too many different combinations of decodings before seeing the hint and the tag saying *Base64*.  If we keep decoding with *Base64*, the 6th repeat shows the complete flag.


## Extra

Made bash script *repeatBase64.sh* to find the flag using `bash64` command.  The `bash64` command can be used to encode or decode text from the command line.  Would like to put this script into a loop to stop repetition of code but for now its 6 bash --decodes all setup to pipe the result from one to the other.

## Solution

*Flag may be different for others due to active competition.*