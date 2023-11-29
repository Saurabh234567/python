from cipherkey import getencryptcipherkey
from message import getencryptmessage


def encryptmessage(message,cipherkey,alphabet):
    encryptedmessage=""
    uppermess=message.upper()
    for currchar in uppermess:
        position = alphabet.find(currchar)
        newpost = position + int(cipherkey)
        if currchar in alphabet:
            encryptedmessage = encryptedmessage + alphabet[newpost]
        else:
            encryptedmessage = encryptedmessage + currchar
    return encryptedmessage

a="ABCDEFGHIJKLMNOPQWRSTUVWXYZ"
c = getencryptcipherkey()
m = getencryptmessage()

print(encryptmessage(m,c,a))