def decrypmessage(encryptedmessage, cipherkey, alphabet):
    decryptedmessage = ""
    uppermessage = encryptedmessage.upper()
    for char in uppermessage:
        if char in alphabet:
            position = alphabet.find(char)
            newpost = position - int(cipherkey)
            decryptedmessage += alphabet[newpost]
        else:
            decryptedmessage += char
    return decryptedmessage