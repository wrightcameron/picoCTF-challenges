# Safe Opener 2

## Problem

What can you do with this file? I forgot the key to my safe but this [file](https://artifacts.picoctf.net/c/292/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

## Notes

The file downloaded SafeOpener.class is obviously a binary java file.  This is proved with the `file` command

```bash
$ file SafeOpener.class 
SafeOpener.class: compiled Java class data, version 52.0 (Java 1.8)
```

Before trying to find out what this binary file does the easiest way to check this file for flag is use the `string` command.  The `string` command parses a binary file and grabs all the plain text from it.  This plain text could be docs, comments, or other plain text left in after compiling.

For this file this is what `string` returns

```bash
$ strings SafeOpener.class 
<init>
Code
LineNumberTable
LocalVariableTable
this
LSafeOpener;
main
([Ljava/lang/String;)V
isOpen
args
[Ljava/lang/String;
keyboard
Ljava/io/BufferedReader;
encoder
Encoder
InnerClasses
Ljava/util/Base64$Encoder;
encodedkey
Ljava/lang/String;
StackMapTable
Exceptions
openSafe
(Ljava/lang/String;)Z
password
SourceFile
SafeOpener.java
java/io/BufferedReader
java/io/InputStreamReader
Enter password for the safe: 
java/lang/StringBuilder
You have  
 attempt(s) left
,picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}
Sesame open
Password is incorrect
SafeOpener
java/lang/Object
java/util/Base64$Encoder
java/lang/String
java/io/IOException
java/lang/System
Ljava/io/InputStream;
(Ljava/io/InputStream;)V
(Ljava/io/Reader;)V
java/util/Base64
getEncoder
()Ljava/util/Base64$Encoder;
Ljava/io/PrintStream;
java/io/PrintStream
print
(Ljava/lang/String;)V
readLine
()Ljava/lang/String;
getBytes
()[B
encodeToString
([B)Ljava/lang/String;
println
append
-(Ljava/lang/String;)Ljava/lang/StringBuilder;
(I)Ljava/lang/StringBuilder;
toString
equals
(Ljava/lang/Object;)Z
```

Quickly skimming the hunch was correct, the flag is contained as picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}

We could have decompiled this file, InteliJ.  But doing strings first got us to the solution faster.

## Solution

picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_0e57c117}
