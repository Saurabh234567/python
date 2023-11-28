def doublealpha(alphabet):
   doublealpha=alphabet+alphabet
   return doublealpha  

def getcipherkey():
    shift=input("enter key(number between 1 to 25)")
    return shift

def getmsg():
    ste=input("enter message to decrypt: ")
    return ste

def decryption(msg,cipherkey,alphabet):
    decrytedtxt=""
    uppertxt=""
    uppertxt=msg.upper()
    for word in uppertxt:
      position=alphabet.find(word)
      newposition=position-int(cipherkey)
      if word in uppertxt:
          decrytedtxt=decrytedtxt+alphabet[newposition]
      else:
          decrytedtxt=decrytedtxt+word
    return decrytedtxt

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=getcipherkey()
m=getmsg()
print(decryption(m,c,alphabet))
