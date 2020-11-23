#!/usr/bin/python3
#the Mode Selection Module
import Ceaser, CeaserCracker, Columnar, ColumnarCracker, Vigenere, VigenereCracker 
from bcolors import bcolors

def choice():
    mode = input(bcolors.OKCYAN+"\rEncrypt or Decrypt? : "+bcolors.ENDC)
    if mode[0].lower() == 'e':
        mode = 'encrypt'
        return mode
    elif mode[0].lower() == 'd':
        mode = 'decrypt'
        return mode
    else:
        print(bcolors.FAIL+"\nQuitting!! Only Accept Encryption or Decryption!\n"+bcolors.ENDC)
        exit()

# Function for the available options selection
def options(argument): 
    if(argument==1):
        print(bcolors.BOLD+bcolors.OKBLUE+"Ready to Encrypt/Decrypt Ceaser Cipher?"+bcolors.ENDC)
        Ceaser.main()
    elif(argument==2):
        print(bcolors.BOLD+bcolors.OKBLUE+"Ready to Encrypt/Decrypt Columnar Cipher?"+bcolors.ENDC)
        Columnar.main()
    elif(argument==3):
        print(bcolors.BOLD+bcolors.OKBLUE+"Ready to Encrypt/Decrypt Vigenere Cipher?"+bcolors.ENDC)
        Vigenere.main()
    elif(argument==4):
        print(bcolors.BOLD+bcolors.OKBLUE+"Excited to Crack Ceaser Cipher?"+bcolors.ENDC)
        CeaserCracker.main()
    elif(argument==5):
        print(bcolors.BOLD+bcolors.OKBLUE+"Excited to Crack Columnar Cipher?"+bcolors.ENDC)
        ColumnarCracker.main()
    elif(argument==6):
        print(bcolors.BOLD+bcolors.OKBLUE+"Excited to Crack Vigenere Cipher?"+bcolors.ENDC)
        VigenereCracker.main()
    else:
        print(bcolors.FAIL+"Quitting!! The Option must be between 1 and 6\n"+bcolors.ENDC)
        exit(0)

# Function to check if the input is INT type
def intInput():
    while True: #Error Handling for the ValueError
        try:
            myKey = int(input(bcolors.OKBLUE+"Choose your Desired Rotation Key Number: "+bcolors.ENDC))
            break
        except ValueError:
            print(bcolors.FAIL+"Only input the Number! Alphabets are not Accepted!"+bcolors.ENDC)
    return myKey