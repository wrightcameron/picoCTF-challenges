# Special

## Problem

Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM) Start your instance to see connection details.

Additional details will be available after launching your challenge instance.

## Notes

Looks like when connecting with ssh the server has a customer "shell" that is run with python.

When issuing ctrl-d this is the error that is thrown.

```python
Traceback (most recent call last):
  File "/usr/local/Special.py", line 19, in <module>
    elif cmd[0] == '/':
IndexError: string index out of range
Connection to saturn.picoctf.net closed.
```

This error looks to be thrown cause no input was given before end of input was used.

When issuing ctrl-c this is the error that is thrown.

```python
Special$  ^CTraceback (most recent call last):
  File "/usr/local/Special.py", line 11, in <module>
    cmd = input("Special$ ")
KeyboardInterrupt
Connection to saturn.picoctf.net closed.
```

- When words are inputed it capitalises the first word like in a sentance
- word are also commands, by the printing of the sh, python may be passing user input to sh.
- Trying to run `/bin/bash` results in it saying "Why go back to an inferior shell?"
- Trying to run `/usr/bin/ls` or other non existiant commands returns "Absolutly not paths like that, please!"
- some commands like `ls` are "spell corrected" to Is
## Solution

*Flag may be different for others due to active competition.*

