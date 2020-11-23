#!/usr/bin/python3
#Cracking Columnar Cipher
import pyperclip, detectEnglish, Columnar, bcolors
from bcolors import bcolors

def main():
    message = input(bcolors.WARNING+"Please input the Message you wish to Decipher:\n"+bcolors.ENDC)
    cracked = ColumnarCrack(message)
    
    if cracked == None:
        print(bcolors.FAIL+'No possible plaintext can be found from this Columnar Cipher!\n'+bcolors.ENDC)
        exit(0)
    else:
        print(bcolors.OKGREEN+cracked+bcolors.ENDC)
        pyperclip.copy(cracked)
    exit(0)

def ColumnarCrack(message):
    print(bcolors.OKCYAN+"\nDeciphering...Press Ctrl-C or Ctrl-D to quit!"+bcolors.ENDC)
    # Brute-force by looping through every possible key.
    for key in range(1, len(message)):
        cracked = Columnar.decryption(key, message)
        #Will ask the user to decide with their human congitive ability to decide the result
        if detectEnglish.isEnglish(cracked):
            print('\nPossible encryption hack:')
            print('Trying key #%s...' % (key))
            print('Key %s: %s' % (key, bcolors.OKBLUE+bcolors.UNDERLINE+cracked[:100])+"\n"+bcolors.ENDC)
            response = input('Press'+bcolors.FAIL+' G '+bcolors.ENDC+'if desired message is found! Else, continue: ')

            if response.strip().upper().startswith('G'):
                return cracked
    return None

# Driver program 
if __name__ == '__main__':
    main()
