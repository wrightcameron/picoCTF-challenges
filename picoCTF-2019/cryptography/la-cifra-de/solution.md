# la cifra de

## Problem

I found this cipher in an old book. Can you figure out what it says? Connect with **nc jupiter.challenges.picoctf.org 32411**.

## Notes

The message from netcating that location is,

```text
Encrypted message:
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo 

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}

Ehk ktryy herq-ooizxetypd jjdcxnatoty ol f aordllvmlbkytc inahkw socjgex, bls sfoe gwzuti 1467 my Rjzn Hfetoxea Gqmexyt.

Tnj Gimjyèrk Htpnjc iy ysexjqoxj dosjeisjd cgqwej yse Gqmexyt Doxn ox Fwbkwei Inahkw.

Tn 1508, Ptsatsps Zwttnjxiax tnbjytki ehk xz-cgqwej ylbaql rkhea (g rltxni ol xsilypd gqahggpty) ysaz bzuri wazjc bk f nroytcgq nosuznkse ol yse Bnretèwp Cousex.

Gplrfdo’y xpcuso butvlky lpvjlrki tn 1555 gx l cuseitzltoty ol yse lncsz. Yse rthex mllbjd ol yse gqahggpty fce tth snnqtki cemzwaxqj, bay ehk fwpnfmezx lnj yse osoed qptzjcs gwp mocpd hd xegsd ol f xnkrznoh vee usrgxp, wnnnh ify bk itfljcety hizm paim noxwpsvtydkse.
```

The challange name is **la cifra de**, and looking through old ciphers there is one called [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Friedman_test).  From a word play standpoint this cipher was also known as **chiffrage indéchiffrable** which matches up with the challange name.

CyberChef does have a decode Vigenere option, but it requires a key which I don't have. The website [decode.fr](https://www.dcode.fr/vigenere-cipher) does have am much better tool for cracking the cipher without the key.  Because this cipher doesn't require the entire message to decode it, and we can already see *hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3x7g996649}* which is going to be *picoCTF{XXXX}* we can just have the site decode just that.  The site has a field for if we know some of the plaintext message.  Filling that field out the flag is found.  THe flag is *picoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}*.

## Solution

Knowing part of the message is *picoCTF{XXXX}*, the website https://www.dcode.fr/vigenere-cipher can crack the message without the key. The flag is picoCTF{b311a50_0r_v1gn3r3_c1ph3r7b996649}

