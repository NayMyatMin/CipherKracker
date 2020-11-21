from bcolors import bcolors

def choice():
    global mode
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