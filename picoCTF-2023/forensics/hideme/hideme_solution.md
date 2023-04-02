# hideme

## Problem

Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here](https://artifacts.picoctf.net/c/261/flag.png).

## Notes

The file is a PNG of the picoCTF logo.  The tag on the challange does say Steganography, the art of putting messages in other media.  So any CLI tools for steganography would be perfered.  To start anaylzing this picture will defer to the notes taken on challanges [[so-meta_solution]], [[extensions_solution]].

Using the `identify -verbose flag.png` command resulted in no flag, atleast in plain text.  Neither did the `strings flag.png` command, though at this point too many flags have been too easy on the flag being plaintext in a binary file.

The commands `hexdump -C flag.png` & `xxd flag.png` can also be used to try hidden messages in the binary code.  Strings just pulls the plain text but `hexdump` and `xxd` will give a larger picture.

To try to find the flag, the stegosuite, a GUI tool for embedding and extracting messages.  It was installed with `sudo apt install stegosuite openjdk-17-jdk`.  The problem is that extracting a secret message requires a password and stegosuite doesn't have a way to brute force that password.

`steghide` another command for hidding messages could be used but it doesn't work for png files.

The `exif` command, used for viewing image meta data is another great tool.  

## Solution

Answer

*Flag may be different for others due to active competition.*

## Resources

- [Steganography](https://en.wikipedia.org/wiki/Steganography)
- [Steganography - A list of useful tools and resources](https://0xrick.github.io/lists/stego/)