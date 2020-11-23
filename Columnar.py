#!/usr/bin/python3
# Transposition Cipher - Columnar
import math, pyperclip, ConvertMode
from bcolors import bcolors

def main():
    mode=ConvertMode.choice() #Choose the Mode
    myKey=ConvertMode.intInput() #Ask for the user input key
    message=input(bcolors.WARNING+"Please enter the message you wish to convert: \n"+bcolors.ENDC)

    if mode == 'encrypt':
        ciphertext = encryption(myKey, message)
        print(bcolors.WARNING+"\nResult of the Columnar Cipher: \n"+bcolors.OKGREEN+ciphertext+'|\n'+bcolors.ENDC)
        pyperclip.copy(ciphertext)

    elif mode == 'decrypt':
        plaintext = decryption(myKey, message)
        print(bcolors.WARNING+"\nResult of the Columnar Cipher: \n"+bcolors.OKGREEN+plaintext+'|\n'+bcolors.ENDC)
        pyperclip.copy(plaintext)
    exit(0)

def encryption(key, message):
    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Loop through each column in ciphertext.
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length.
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key # move currentIndex over

    return ''.join(ciphertext)


def decryption(key, message):
    # columns in transposition grid
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key # rows" in grid

    # shaded boxes" in last column
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column
    plaintext = [''] * numOfColumns

    column = 0  # The column and row variables point to where in the grid the next
    row = 0     # character in the encrypted message will go.

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        #When No columns OR  at a shaded box, go back to the first column and the next row
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

# Driver program 
if __name__ == "__main__": 
    main()