def getCipherkey():
    key =-1
    while key<1 or key>25:
        key = int(input("Please Enter a Cipher key (whole number from 1-25):"))
    return key

def getMessage():
    msg = input("Please enter your Encrypted Message:")
    return msg

def decryptMessage(message,cipherKey,alphabet):
    decryptedMessage=""
    upperMess=message.upper()
    for currchar in upperMess:
        position = alphabet.find(currchar)
        newpost = position - cipherKey
        if currchar in alphabet:
            decryptedMessage = decryptedMessage + alphabet[newpost]
        else:
            decryptedMessage = decryptedMessage + currchar
    return decryptedMessage

a="ABCDEFGHIJKLMNOPQWRSTUVWXYZ"
c = getCipherkey()
m = getMessage()

print("Your Decrypted Message : ",decryptMessage(m,c,a))