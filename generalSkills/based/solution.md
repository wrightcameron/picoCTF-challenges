# Based
## Problem
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 29221.`

## Notes
The python script created is not unit tested and is kind of brute forced, so extra work could go into improving this script.

## Solution
The solution to this was to convert the binary, octo, and hex to ASCII characters.  The netcat tcp connection though required that these be solved under 45 seconds each.  So using a python program I was able to take the input, process it, and return the word.

Took alittle longer than normal as I didn't know octo, and hex were to come after decimal.
