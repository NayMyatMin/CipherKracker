#!/usr/bin/python3
import pyperclip, ConvertMode
from bcolors import bcolors

def main():
    mode=ConvertMode.choice() #Choose the Mode
    key=ConvertMode.intInput() #Ask for the user input key
    message=input(bcolors.WARNING+"Please enter the message you wish to convert: \n"+bcolors.ENDC)

    # Every possible symbol that can be converted:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
    converted = '' # Stores the converted message

    for symbol in message:
        # Only symbols in the `SYMBOLS` string can be converted
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode=='encrypt':
                convertedIndex = symbolIndex + key
            elif mode=='decrypt':
                convertedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if convertedIndex >= len(SYMBOLS):
                convertedIndex = convertedIndex - len(SYMBOLS)
            elif convertedIndex < 0:
                convertedIndex = convertedIndex + len(SYMBOLS)

            converted = converted + SYMBOLS[convertedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            converted = converted + symbol

    #Print out the result
    print(bcolors.WARNING+"\nResult of the Ceaser Cipher: \n"+bcolors.OKGREEN+converted+bcolors.ENDC)
    pyperclip.copy(converted)
    exit(0)

# Driver program 
if __name__ == "__main__": 
    main()