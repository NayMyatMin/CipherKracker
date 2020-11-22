#Vigenere Cipher
import math, pyperclip, ConvertMode
from bcolors import bcolors

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    mode=ConvertMode.choice() #Choose the Mode

    myKey = input(bcolors.OKBLUE+"Please input your key: "+bcolors.ENDC)
    message=input(bcolors.WARNING+"Please enter the message you wish to convert: \n"+bcolors.ENDC)

    if mode == 'encrypt':
        converted = encryption(myKey, message)
    elif mode == 'decrypt':
        converted = decryption(myKey, message)

    print(bcolors.WARNING+"\n%sed message with Vigenere Cipher:"% (mode.title())+bcolors.ENDC )
    print(bcolors.OKGREEN+converted+"\n"+bcolors.ENDC)
    pyperclip.copy(converted)
    exit(0)

def encryption(key, message):
    return convertMessage(key, message, 'encrypt')

def decryption(key, message):
    return convertMessage(key, message, 'decrypt')


def convertMessage(key, message, mode):
    converted = [] # Stores the encrypted/decrypted message string.

    keyIndex = 0
    key = key.upper()

    for symbol in message: # Loop through each symbol in message.
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # Subtract if decrypting.

            num %= len(LETTERS) # Handle any wraparound.

            # Add the encrypted/decrypted symbol to the end of converted:
            if symbol.isupper():
                converted.append(LETTERS[num])
            elif symbol.islower():
                converted.append(LETTERS[num].lower())

            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting.
            converted.append(symbol)

    return ''.join(converted)

# Driver program 
if __name__ == "__main__": 
    main()