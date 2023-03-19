#  Permissions

## Problem

Can you read files in the root file?

Additional details will be available after launching your challenge instance.

## Notes

Running the instance gives access to ssh to Linux server.  The challange says read file in the root file, which sounds like the root dir.  Which anyone can go to by typing `cd /`.   The files by default give everyone permission to read even if only root can modify.

This system looks to be a docker container, with a `.dockerenv` file and a `/challanges/` directory.  For docker images the application is usually installed off of the root dir not in `/opt/`.  Opening that directory showed one file *metadata.json*, which contained the flag in a json object.

```json
{"flag": "picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}", "username": "picoplayer", "password": "GhHrPQ2+zL"}
```

## Solution

picoCTF{uS1ng_v1m_3dit0r_3dd6dcf4}

*Flag may be different for others due to active competition.*