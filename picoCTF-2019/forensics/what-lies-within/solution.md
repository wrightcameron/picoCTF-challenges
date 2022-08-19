# What Lies Within

## Problem

There's something in the [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png). Can you retrieve the flag?

## Links

* [building](https://jupiter.challenges.picoctf.org/static/011955b303f293d60c8116e6a4c5c84f/buildings.png)

## Notes

First checked the file with vim, there wasn't any text that would give away the flag.  The next thing to try was decoding the file from base64. `base64 --decode buildings.png | grep pico`.  This didn't find anything.  I then tried downloading tools `stegosuite` and `steghide` but didn't find way's to check for hidden messages with those tools.

Using [cyberchef](https://cyberchef.org/#recipe=Extract_LSB('R','G','B','','Row',0)), there are multiple algorithems for checking for [Steganography](https://en.wikipedia.org/wiki/Steganography#Digital_messages).

After Bacon Cipher, the next algorithem was [Extract LSB](https://en.wikipedia.org/wiki/Steganography#Digital_messages).  Having the color pallet of red, green, and blue, the flag will show up in the output.  The flag is picoCTF{h1d1ng_1n_th3_b1t5}

## Solution

Using the LSB Extract algorithem on the cyberchef website, the picture can be uploaded.  The uploaded picture using the LSB Extract algorithem and selecting R, G,B the flag is picoCTF{h1d1ng_1n_th3_b1t5}

