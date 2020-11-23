#!/usr/bin/python3
#library file for the Mode Selection
import Ceaser, CeaserCracker, Columnar, ColumnarCracker, Vigenere, VigenereCracker 
from bcolors import bcolors

def choice():
    mode = input(bcolors.OKCYAN+"\nEncrypt or Decrypt? : "+bcolors.ENDC)
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
        Ceaser.main()
    elif(argument==2):
        Columnar.main()
    elif(argument==3):
        Vigenere.main()
    elif(argument==4):
        CeaserCracker.main()
    elif(argument==5):
        ColumnarCracker.main()
    elif(argument==6):
        VigenereCracker.main()
    else:
        print(bcolors.FAIL+"Quitting!! The Option must be between 1 and 6\n"+bcolors.ENDC)
        exit(0)