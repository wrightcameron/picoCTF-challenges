# vault-door-4

## Problem

This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java)

## Links

* [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/09d3002ae349631324a17e2255ae8df2/VaultDoor4.java)

## Notes

This challange is easier that vault-door-3.  The thing is that this problem is just converting the flag to a byte array, and comparing that byte array with another byte array that is exactly the flag.

So the solution is just to convert that byte array back to a string, which is very easy referencing the Java API String class.  A String in java can be created by passing a byte array to the constructor.  So the solution is just to do `String str=new String(bytes);`.  Java solution contained in current directory.

## Solution

Flag is picoCTF{jU5t_4_bUnCh_0f_bYt3s_c194f7458e}

