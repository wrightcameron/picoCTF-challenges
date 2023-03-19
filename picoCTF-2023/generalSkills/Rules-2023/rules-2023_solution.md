# Rules 2023

## Problem

Read the rules of the competition and get a little bonus! [Rules](https://picoctf.org/competitions/2023-spring-rules.html)

## Notes

The link leads to the html site rules.  While I would say reading rules is important, as well as reading comprehension.  Knowing how to use Linux commands to quickly find solutions is also good thing to know.

If the flag is actually on the page either in the text or html, `curl` and `grep` will quickly find it.  With the command,  `curl https://picoctf.org/competitions/2023-spring-rules.html | grep picoCTF{`, the flag is found.

~~Looks like using curl and grep was the best solution.~~   The flag wasn't in any visible text, but instead the alt text for a image.  The image was an image of the flag as well, so manually finding it would have worked as well.  Thankfully picoCTF set the alt text for accessibity.

> The alt attribute hold a text description of the image, which isn't mandatory but is incredibly useful for accessibility -- screen readers read this description out to their users so they known what the image means. Alt text is also displayed on the page if the image can't be loaded for some reason: for example, network errors, content blocking, or linkrot.

## Solution

picoCTF{h34rd_und3r5700d_4ck_cba1c711}

*Flag may be different for others due to active competition.*
