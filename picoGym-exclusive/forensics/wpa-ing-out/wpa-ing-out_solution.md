# WPA-ing Out

## Problem

I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, especially if I used the same wireless network password as one in the rockyou.txt credential dump. Use this '[pcap file](https://artifacts.picoctf.net/c/8/wpa-ing_out.pcap)' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.

## Links

* [pcap file](https://artifacts.picoctf.net/c/8/wpa-ing_out.pcap)

## Notes

A .pcap file is a packet capture log file.  This file is associated with Wireshark and that will be needed to solve this challange.

### Hint 1

"Finding the IEEE 802.11 wireless protocol used in the wireless traffic packet capture is easier with wireshark, the JAWS of the network."

This first hint doesn't tell you much, opening up the file with Wireshark you can already see that the protocol for most of the traffic is protcol 802.11
### Hint 2

"Aircrack-ng can make a pcap file catch big air...and crack a password."  

Aircrack-ng is a tool for cracking WPA/WPA2 wire access points.  If the handshake for the password has been done, this cli tool will use brute force to crack the passcode.

Never used this tool before, and so can't comment on the many other features that this tool can do.  But for this challange just passing the password list rockyou.txt and the pcap file to the command as,

```bash
$ aircrack-ng -w rockyou.txt wpa-ing_out.pcap
Reading packets, please wait...
Opening wpa-ing_out.pcap
Read 23523 packets.

   #  BSSID              ESSID                     Encryption

   1  00:5F:67:4F:6A:1A  Gone_Surfing              WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening wpa-ing_out.pcap
Read 23523 packets.

1 potential targets

                               Aircrack-ng 1.6 

      [00:00:00] 1653/10303727 keys tested (7877.29 k/s) 

      Time left: 21 minutes, 47 seconds                          0.02%

                          KEY FOUND! [ mickeymouse ]


      Master Key     : 61 64 B9 5E FC 6F 41 70 70 81 F6 40 80 9F AF B1 
                       4A 9E C5 C4 E1 67 B8 AB 58 E3 E8 8E E6 66 EB 11 

      Transient Key  : 89 F6 77 00 A8 EC 4A 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 

      EAPOL HMAC     : 65 2F 6C 0E 75 F0 49 27 6A AA 6A 06 A7 24 B9 A9
```

Wireshare isn't really great for this problem, cause unless you know how to pick the password out of an entire log quickly, `aircrack-ng` can find it very quickly.

## Solution

The challange gives a pcap file, which contains network traffic.  Using the cli tool `aircrack-ng` the flag can quickly be found with the rockyou.txt credential dump.  The command to find the password is `aircrack-ng -w rockyou.txt wpa-ing_out.pcap`.  It will find the password in seconds.  The password is mickymouse and when put it between picoCTF{mickeymouse} the CTF is correct.

## Further Study

Read up on entire `aircrack-ng` suite to learn how to scan and crack WAPs.

## Resources

* [Cracking WPA/WPA2 with Aircrack-ng for n00bs](https://cyberrunner.medium.com/for-n00bs-cracking-wpa-wpa2-with-aircrack-ng-988e8dd73668)
* [zacheller/rockyou Github repo](https://github.com/zacheller/rockyou)
