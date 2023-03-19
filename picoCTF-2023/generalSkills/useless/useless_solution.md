# useless

## Problem

There's an interesting script in the user's home directory

## Notes

Running the instance gives access to ssh to Linux server.  In the home dir of the picoplayer user is a bash script called useless.

```bash
#!/bin/bash
# Basic mathematical operations via command-line arguments

if [ $# != 3 ]
then
  echo "Read the code first"
else
	if [[ "$1" == "add" ]]
	then 
	  sum=$(( $2 + $3 ))
	  echo "The Sum is: $sum"  

	elif [[ "$1" == "sub" ]]
	then 
	  sub=$(( $2 - $3 ))
	  echo "The Substract is: $sub" 

	elif [[ "$1" == "div" ]]
	then 
	  div=$(( $2 / $3 ))
	  echo "The quotient is: $div" 

	elif [[ "$1" == "mul" ]]
	then
	  mul=$(( $2 * $3 ))
	  echo "The product is: $mul" 

	else
	  echo "Read the manual"
	 
	fi
fi
```

The script is very simple.  It uses `$#` and `$1, $2, $3` for finding the number of pramaters passed in and then using those parameters at those indexes.

One of the else conditions at the bottom mentions to read the manual.  In Linux the manual are the man pages, accessed with `man`.  Using `man useless` opens up a man page for the script.  At the bottom of  the man page is the flag.

Note: custom scripts usually don't come with their own man page.  The man page with the flag might be in the dir `/usr/local/share/man/*`

## Solution

picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_1155}

*Flag may be different for others due to active competition.*
