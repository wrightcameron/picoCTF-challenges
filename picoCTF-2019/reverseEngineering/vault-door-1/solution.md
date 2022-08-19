# vault-door-1

## Problem

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java)

## Links

* [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/29b91e638ccbd76aaa8c0462d1c64d8d/VaultDoor1.java)

## Solution

This Java file in this challange is very similar to the previous challange "VaultDoor-training."  In this new file the checkPassword method instead of having the flag as a string in order.  Has a bunch of password.charAt(x) == 'x' statements that are the characters of the flag but out of order.

Instead of changing the Java file to print the letters in the correct order, I highlighted all the lines and sorted them ascending.  Then it was just going down the lines copying each character.

The flag is picoCTF{d35cr4mbl3_th3_cH4r4cT3r5_ff63b0}

