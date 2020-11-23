#!/usr/bin/python3
#the Mode Selection Module
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

# Function to check if the input is INT type
def intInput():
    while True: #Error Handling for the ValueError
        try:
            myKey = int(input(bcolors.OKBLUE+"Choose your Desired Rotation Key Number: "+bcolors.ENDC))
            break
        except ValueError:
            print(bcolors.FAIL+"Only input the Number! Alphabets are not Accepted!"+bcolors.ENDC)
    return myKey