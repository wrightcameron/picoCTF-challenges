# flag shop
## Problem
There's a flag shop selling stuff, can you buy a flag? `Source`. Connect with `nc jupiter.challenges.picoctf.org 4906.`

## Links
* [Source] (https://jupiter.challenges.picoctf.org/static/64e724ad327f83ad833d9c6baa072b1f/store.c)

## Notes
Observations during problem

## Solution
The challenge gives the source code of the netcat tcp connection made to the server.  When looking at the code you can see that the flag is stored in a text file, and getting to the text file only happens when a user can buy a flag that costs more money than the starting balance.  The balance also is not modified in anyway to add funds, only take them away with buying lesser flags.  

The hint mentions two's complement, which means the most significant bit is used to determine if the binary number is positive or negative. This means that the way to solve this issue is to cause an input from one of the three scanf() must cause an integer overflow, where our integer will become negative if its too large.

Of the scanf() the one needed to solve this problem is the one asking for how many flags we want to buy.  Giving it 1000000000 will cause an integer overflow, it will cause that overflow when that number is multiplied by 900.  After that number is inputted the users balance will be very large and will have no problem buying the flag, just follow the steps to buy it and the flag will be shown.  For me it was picoCTF{m0n3y_bag5_9c5fac9b}
