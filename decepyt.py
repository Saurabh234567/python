from message import getmessage
from cipherkey import getcipherkey
from encrypt import encryptmessage

def decryptmessage(encryptmessage,cipherkey,alphabet):
    print(f"Encrypted message is = ",encryptmessage)
    decryptedmessage=""
    uppermess=encryptmessage.upper()
    for currchar in uppermess:
        position = alphabet.find(currchar)
        newpost = position - int(cipherkey)
        if currchar in alphabet:
            decryptedmessage = decryptedmessage + alphabet[newpost]
        else:
            decryptedmessage = decryptedmessage + currchar
    return decryptedmessage

a="ABCDEFGHIJKLMNOPQWRSTUVWXYZ"
c = getcipherkey()
m = getmessage()
e= encryptmessage(m,c,a)
print(f"Decrypted message is = "+decryptmessage(e,c,a))