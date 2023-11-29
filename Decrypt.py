from cipherkey import getCipherkey
from encrypt import encryptMessage
from message import getmessage
from dfunc import getDoubleAlphabet

def decryptMessage(enmessage, cipherKey, alphabet):
    print("The Encypted Message : ", enmessage)
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

mess=getmessage()
key=getCipherkey()
alpha=getDoubleAlphabet()
e=encryptMessage(mess,key,alpha)

print("The Decrypted Message : ",decryptMessage(e,key,alpha))