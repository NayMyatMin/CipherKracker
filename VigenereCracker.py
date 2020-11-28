#!/usr/bin/python3
#Cracking Vigenere Cipher
import detectEnglish, Vigenere, pyperclip
from bcolors import bcolors

def main():
    message= input(bcolors.WARNING+"Please input the cipher you wish to Decipher:\n"+bcolors.ENDC)
    cracked = VigenereCrack(message)

    if cracked == None:
        print(bcolors.FAIL+'No possible plaintext can be found from this Vigenere Cipher!\n'+bcolors.ENDC)
        exit(0)
    else:
        print(bcolors.OKGREEN+cracked+bcolors.ENDC)
        pyperclip.copy(cracked)
    exit(0)

def VigenereCrack(message):
    with open('Wordlist.txt','r') as fo:
        words = fo.readlines()
  
    for word in words:
        word = word.strip() # Remove the newline at the end.
        cracked = Vigenere.decryption(word, message)
        #Will ask the user to decide with their human congitive ability to decide the result
        if detectEnglish.isEnglish(cracked, wordPercentage=40):
            print('\nPossible encryption hack:')
            print('Key ' + str(word) + ': ' + bcolors.OKBLUE+bcolors.UNDERLINE+cracked[:100]+"\n"+bcolors.ENDC)
            response = input('Press'+bcolors.FAIL+' G '+bcolors.ENDC+'if desired message is found! Else, continue: ')

            if response.strip().upper().startswith('G'):
                return cracked
    return None

if __name__ == '__main__':
    main()
