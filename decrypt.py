from cipherkey import getcipherkey
from message import getmessage


def decryptmessage(message,cipherkey,alphabet):
    decryptedmessage=""
    uppermess=message.upper()
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

print(decryptmessage(m,c,a))