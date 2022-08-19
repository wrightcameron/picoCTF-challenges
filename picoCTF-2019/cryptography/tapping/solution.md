# Tapping

## Problem

Theres tapping coming in from the wires. What's it saying nc jupiter.challenges.picoctf.org 21610.

## Solution

Tapping, wires; this problem is very much about [Morse Code](https://en.wikipedia.org/wiki/Morse_code).  Using netcat to go to the site proves that, and the string returned from that destination is Morse Code.  Instead of solving this with Wikipedia, [CyberChef](https://cyberchef.org). has an operation to solve Morse.

```text
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ...-- ----. ----- ..--- ----- .---- ----. ..... .---- ----. }
```

Becomes `PICOCTFM0RS3C0D31SFUN3902019519`, { } need to be added back in for a flag that is PICOCTF{M0RS3C0D31SFUN3902019519}

