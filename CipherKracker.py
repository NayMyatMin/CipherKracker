#!/usr/bin/python3
__author__ = "Nay Myat Min"
__copyright__ = "Computer and Network Security, Mahidol"
__version__ = "1.0.0"
__maintainer__ = "Nay Myat Min"
__email__ = "nay.min@student.mahidol.ac.th"
__status__ = "Development"

import ConvertMode
from signal import signal, SIGINT
from sys import exit
from bcolors import bcolors

def main():
    signal(SIGINT, handler) #run the handler() function when SIGINT is recieved
    while True:
        header()
        selection()
    exit(0)

def header():
    print(bcolors.OKBLUE + "\n######################################" + bcolors.ENDC)
    print(bcolors.OKBLUE + "#### Cipher Kracker by NayMyatMin ####" + bcolors.ENDC)
    print(bcolors.OKBLUE + "######################################\n" + bcolors.ENDC)

def selection():
    print('''Option 1 - Encryption/Decryption with Ceaser Cipher\r
Option 2 - Encryption/Decryption with Columnar Cipher\r
Option 3 - Encryption/Decryption with Vigenere Cipher\r
Option 4 - Cracking Ceaser Cipher\r
Option 5 - Cracking Columnar Cipher\r
Option 6 - Cracking Vignere Cipher''')
    #Error Handling for the ValueError
    while True:
        try:
            argument=int(input(bcolors.WARNING+"Please Select your Option Number: "+bcolors.ENDC))
            break
        except ValueError:
            print(bcolors.FAIL+"Only input the Number! Alphabets are not Accepted!"+bcolors.ENDC)
    ConvertMode.options(argument)

def handler(signal_received, frame):
    # Handle any cleanup here
    print('\nCTRL-C detected. Exiting gracefully\n')
    exit(0)

# Driver program 
if __name__ == "__main__": 
    main()


    