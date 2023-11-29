from cipherkey import getdecryptcipherkey
from message import getdecryptmessage


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
c = getdecryptcipherkey()
m = getdecryptmessage()

print(decryptmessage(m,c,a))