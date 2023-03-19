# Transformation
## Problem
I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Notes
The text returned by the enc link looks to be either Japanese or Chinese.

PUtting it into a translater, it reconizes japanese but with some symbols still remianing, so I 
think that this message is a combination of Japanese and another langauge.

灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽 -> 灩捯䍔䙻楴玛獴 Bushel 摟弸彥㝽

灩捯䍔䙻楴玛獴 -> A dragonfly

摟弸彥㝽 -> Hold your arms around him

The next thing to look at is the python code that they gave.
```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

This looks to be a list comprehension for loop that is using ascii decimals and shiftign them plus
adding to them to build a new string.

If I expand the loop it would look like this.
```python
output = ''
for i in range(0, len(flag), 2):
	j = chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
        output.join(j)
```

The for loop is starting from 0, and incrementing by 2 to length of flag

Then the ord(flag[i] << 8) means we get the decimal of the character located at index i and being bit shifted to the left 8.  This decimal is added to the other decimal gained from index + 1 of flag
list.

The result of these two decimals is added together and the character is found from that new decimal.

灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽

What if we break down this comment symbol by symbol


What if we reverse engineered that the text should be.  After all they should all start with picoCTF.  If I can find what picoCTF is it may be easier to convert the rest.

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

```python
output = ''
for i in range(0, len(flag), 2):
	j = chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
        output.join(j)
```

Order of operations,
bit shift comes firest,
then the addition

but this also does plus 1 and it start looping from 0 to size of string.

WHat if we started from the top to the bottom, would the i+1 even matter

fn = (a << 8) + a+1

a+1 - a >> 8

灩捯䍔䙻

灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽

灩: 28777
捯: 25455
䍔: 17236
䙻: 18043
ㄶ: 12598
形: 24418
楴: 26996
獟: 29535
楮: 26990
獴: 29556
㌴: 13108
摟: 25695
潦: 28518
弸: 24376
彥: 24421
ㄴ: 12596
ㅡ: 12641
て: 12390
㝽: 14205


p: 112
i: 105
c: 99
o: 111
C: 67
T: 84
F: 70
{: 123
灩: 28777
捯: 25455
䍔: 17236
䙻: 18043
灩捯䍔䙻


The function is wrong, but the path is correct.  We don't care translating all we care about is the bit shifting and making sure the function is correct.

From getting the decimals for both I can see that the function needs to produce 112 first, so out function should look something like

f(12) = 28777 - 25455 >> 8

p: 112
c: 99
C: 67
F: 70
1: 49
_: 95
i: 105
s: 115
i: 105
s: 115
3: 51
d: 100
o: 111
_: 95
_: 95
1: 49
1: 49
0: 48
7: 55
Result: 'pcCF1_isis3do__1107'

WE know the result and we know the starting so we can use both to find the solution, it would be
28777 - (112 << 8) = 105

## Solution

The chinese text returned doesn't matter, what matters is we always know that the first couple 
characters of the flag is picoCTF{, using that we can see that the python code given to us is
the encryption function.  Expanding the encryption function we can print out the decimals of the 
message before and after to get a better idea of if we are heading in the right direction.

This problem is easier if you have some paper and can solve the equation.  The hard part is 
the encryption cuts the string in half by adding the second character to the first.  It's been a 
while since algebra so at the moment I didn't solve for x and y, but we have the entire encrypted
message and solving for n instead of n+1 we can get every other character of the original message.
Knowing what x and f(x) is we can solve for the messing value, and then using either paper or
a simple loop we can stitch the message back together.
