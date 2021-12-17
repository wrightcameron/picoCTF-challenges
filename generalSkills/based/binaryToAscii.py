import sys
import re

def convertByteToASCII(byte: str) -> str:
    return chr(int(byte, 2))

def convertDecimalToASCII(oct: str) -> str:
    return chr(int(oct, 8))

def convertHexToASCII(hex: str) -> str:
    return chr(int(hex, 16))

if __name__ == "__main__":
    # Convert the binary to ascii
    line = input("Type binary string\n")
    match = re.findall(r'[01]*', line)
    binaryString = ""
    for x in match:
        binaryString += x
    print(binaryString)
    for x in range(0, len(binaryString), 8):
        print(convertByteToASCII(binaryString[x:x+8]))
    
    # Convert the octo to ascii 
    line = input("Paste octo string\n")
    match = re.findall(r'[\d]*', line)
    numberString = ""
    for x in match:
        numberString += x
    print(numberString)
    for x in range(0, len(numberString), 3):
        print(convertDecimalToASCII(numberString[x:x+3]))

    # Convert the hex to ascii
    line = input("Paste hex string\n")
    match = re.findall(r'[\dabcdef]*', line)
    hexString = ""
    for x in match:
        hexString += x
    print(hexString)
    for x in range(0, len(hexString), 2):
        print(convertHexToASCII(hexString[x:x+2]))
    print("Exiting")