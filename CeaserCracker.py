#!/usr/bin/python3
#Cracking Ceaser Cipher
import pyperclip, detectEnglish, Columnar, bcolors
from bcolors import bcolors

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    message= input(bcolors.WARNING+"Please input the Message you wish to Decipher:\n"+bcolors.ENDC)
    
    for key in range(len(SYMBOLS)):
        # Set cracked to the blank string, so previous iteration's value for cracked is cleared.
        cracked = ''
        # Loop through each symbol in `message`:
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                crackedIndex = symbolIndex - key
                # Handle the wrap-around:
                if crackedIndex < 0:
                    crackedIndex = crackedIndex + len(SYMBOLS)
                # Append the decrypted symbol:
                cracked = cracked + SYMBOLS[crackedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                cracked = cracked + symbol
        # Possible Decryption
        print('Key #%s: %s' % (key, cracked))

# Driver program 
if __name__ == "__main__": 
    main()