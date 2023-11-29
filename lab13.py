import math
def getmsg():
    ste=input("enter message to encrypt/decrypt: ")
    return ste

def getcipherkey():
    shift=int(input("enter key(number between 1 to 25): "))
    while shift<1 or shift>25:
        print("enter valid key")
        break
    else:
        return shift

def encryption(msg,cipherkey,alphabet):
    encrytedtxt=""
    uppertxt=""
    uppertxt=msg.upper()
    for word in uppertxt:
        position=alphabet.find(word)
        newposition=position+(cipherkey)
        if word in uppertxt:
            encrytedtxt=encrytedtxt + alphabet[newposition]
        else:
            encrytedtxt=encrytedtxt + word
    return encrytedtxt

def decryption(msg,cipherkey,alphabet):
    decrytedtxt=""
    uppertxt=""
    uppertxt=decrytedtxt.upper()
    for word in uppertxt:
      position=alphabet.find(word)
      newposition=position-(cipherkey)
      if word in uppertxt:
          decrytedtxt=decrytedtxt+alphabet[newposition]
      else:
          decrytedtxt=decrytedtxt+word
    return decrytedtxt

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
m=getmsg()
c=getcipherkey()
print(encryption(m,c,alphabet))
print("do you want to decrypt your msg?")
ans=input("y/n: ")
if ans=="y" or ans=="Y":
    dciphertxt=getmsg()
    dcipherkey=getcipherkey()
    print(decryption(dciphertxt,dcipherkey,alphabet))
else:
    print("thank you!!")
    
    