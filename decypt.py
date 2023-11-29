
def getcipherkey():
    key = input("please enter a key (whole number from 1-25): ")
    return key

def getmessage():
    mess = input("please enter your msg to decrypt:   ")
    return mess

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