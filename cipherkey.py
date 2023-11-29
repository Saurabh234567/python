def getCipherkey():
    key = input("Enter the crypto-key Number between 1 - 26 to encrypt: ")
    if key.isdigit():
        key = int(key)
        if 0 < key < 26:
            return key
        else:
            print("Enter the value between 1 - 26 to encrypt !!!!!")
            return getCipherkey()
    else:
        print("Entered Crypto-key is not numeric Kindly redo :-(")
        return getCipherkey()
