# Chrono

## Problem

How to automate tasks to run at intervals on linux servers?

## Notes

Running the instance gives access to ssh to Linux server.  First thought was the flag was in `/etc/system/systemd/*` where all the `systemctl` files would be.  `grep` is a great tool for searching text file contents.Using `grep "picoCTF*" * -R` returned no results.  

Looking at the prompt again it says *intervals*, so it means cron.  Using command `crontab -l` will show cron jobs for current user *picoplayer*.  Using that command showed nothing but there might be cronjobs for the system aka root.  Running command `grep "pico" cron* -R` from dir `/etc/` found the flag in file *crontab*.  The flag was found inside.

## Solution

 picoCTF{Sch3DUL7NG_T45K3_L1NUX_1d781160}

*Flag may be different for others due to active competition.*