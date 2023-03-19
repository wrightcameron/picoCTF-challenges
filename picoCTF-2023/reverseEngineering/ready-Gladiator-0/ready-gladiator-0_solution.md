# Ready Gladiator 0

## Problem

Can you make a CoreWars warrior that always loses, no ties?

Your opponent is the Imp. The source is available [here](https://artifacts.picoctf.net/c/309/imp.red). If you wanted to pit the Imp against himself, you could download the Imp and start your own corewars server.



## Notes

Downloading the file shows the contents of show.

```redcode
;redcode
;name Imp Ex
;assert
mov 1, 2
end
```

The challanges shows `nc saturn.picoctf.net 52128 < imp.red` to send the file to the server.  Sending the file shows that its reading the file and using that to determine the winner/loser.

Looking up **redcode** on google shows results on a competative game where players submit assemly like code that's purpose is to defeat the other players redcode.

Resources included at bottom of the page contains info and getting started on understanding this game and language.

### Getting the redcode to lose

Modifying the file at random does show that some parts of the syntax are required.  I did change the move from `mov 0, 1` to `mov 1, 2`.

```redcode
;redcode
;name Imp Ex
;assert
mov 1, 2
end
```

Here is the the results

```bash
cwright@cam-xps:~/Downloads$ nc saturn.picoctf.net 56168 < imp.red
;redcode
;name Imp Ex
;assert
mov 1, 2
end
Submit your warrior: (enter 'end' when done)

Warrior1:
;redcode
;name Imp Ex
;assert
mov 1, 2
end

Warning in line 3: ';assert'
        Invalid ';assert' parameter
Warning:
        Missing ';assert'. Warrior may not work with the current setting
Number of warnings: 2

Rounds: 100
Warrior 1 wins: 0
Warrior 2 wins: 100
Ties: 0
You did it!
picoCTF{h3r0_t0_z3r0_4m1r1gh7_a220a377}
```

### Understanding the ~~lose~~ win?

The above seems to have won cause based on what `MOV 0, 1` does.  THis command is an instruction that tells the Imp to copy itself from its current address to a new address.  By changing it to `mov 1, 2` it now can't copy itself and eventually the opponent will find the original Imp and defeat it.

## Solution

picoCTF{h3r0_t0_z3r0_4m1r1gh7_a220a377}

*Flag may be different for others due to active competition.*

## Resources

* [Wikipedia: Core War](https://en.wikipedia.org/wiki/Core_War)
* [# Beginner's guide to Redcode](https://corewars.org/docs/guide.html)
