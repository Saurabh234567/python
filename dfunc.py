#definition argument and concatenates, or combines
import string

def getDoubleAlphabet():
    alphabet=string.ascii_letters + string.digits + string.punctuation
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet