# vault-door-3

## Problem

This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)

## Links

* [vaultDoor3.java](https://jupiter.challenges.picoctf.org/static/a648ca6dd275b9454c5d0de6d0f6efd3/VaultDoor3.java)

## Notes

The java file VaultDoor3.java has the same main method as challange Vault Door 1 & 2.  The difference for this file is the checkPassword method.  This one is composed of a bunch of foor loops modifying the password string.  At the end of the checkPassword method is a string it compares the buffer with, this string while looking like the flag isn't it.  But if the code is modified where all the loops run backwards the string that would be used to compare should print out the acual flag.

```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18gb41_u_4_mfr340");
    }
```

This did work out and the evntual code I will include in the directory has two methods.  THe original checkPassword method and the modified one.  Having the original method allows a check to see if the generated flag is correct before checking on picoCTF.

```java
    public String generateFlag(String password){
        if (password.length() != 32) {
            return null;
        }
        char[] buffer = new char[32];
        int i;
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        for (i=16; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=8; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        return new String(buffer);
    }
```

## Solution

The flag can be found by rewriting the checkPassword method to build the flag off the string it compares it too.  THe for loops could be left alone cause each one would do the same operation forward and backwards.  Each index in the loop doesn't effect any other of its neighboors in the entire char array.  So the solution is to just reorder the loops from last to first and the flag will be generated.  Then just surround it with the pico{}.  The flag is picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_1fb380}
 
