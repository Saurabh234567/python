from cipherkey import getCipherkey
from encrypt import encryptMessage
from message import getmessage


def decryptMessage(enmessage, cipherKey, alphabet):
    print("the encypted message : ", enmessage)
    decMessage=""
    upperMessage=enmessage.upper()
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
m=getmessage()
e=encryptMessage(m,c,a)
print(e)

print(decryptMessage(e,c,a))


#m=input("Enter the Encrypted foramt of the message: ")
#print(decryptMessage(m,c,a))
    