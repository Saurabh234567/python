from cipherkey import getcipherkey
from message import getmessage


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

