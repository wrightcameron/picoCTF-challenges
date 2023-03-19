# Shark on wire 1

## Problem

We found this [packet capture.](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap) Recover the flag.

## Links

* [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap)

## Notes

The packet capture can be opened with wireshark as `wireshark capture.pcap &`.  The second hint mentions streams.  Some of these protocals like tcp and udp don't send all the information at once, they send a stream of data.  Right clicking on some protocols there are some hidden messages like `picoCTF{N0t_a_fLag}`.  But even though it says this isn't the flag, its not.  The message is hidden in another stream.

In the top ribben Analyze -> Follow -> UDP Stream.  The new window will show all udp streams and on the right bottom side you can click through all streams.  This saves the headack of trying to find them and filtering all the packets on the main window.  Clicking through all the streams eventuall one stream will have the flag picoCTF{StaT31355_636f6e6e}


## Solution

The flag is found in a udp stream, using wiresharks follow UDP stream the flag is found, the flag is picoCTF{StaT31355_636f6e6e}

