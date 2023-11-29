
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage=""
    upperMessage=message.upper()
    for currCharacter in upperMessage:
        position=alphabet.find(currCharacter)
        newPosition =  position + int(cipherKey)
        if currCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currCharacter
    return encryptedMessage

