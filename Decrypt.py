from CipherKey import getCipherkey
from encrypt import encryptMessage


def decryptMessage(message, cipherKey, alphabet):
    decMessage=""
    upperMessage=message.upper()
    for curMessage in upperMessage:
        position=alphabet.find(curMessage)
        newPosition = position - int(cipherKey)
        if curMessage in alphabet:
            decMessage=decMessage + alphabet[newPosition]
        else:
            decMessage= decMessage + curMessage
    return decMessage


a="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

c=getCipherkey()
m=input("Enter the Encrypted foramt of the message: ")
print(decryptMessage(m,c,a))
    