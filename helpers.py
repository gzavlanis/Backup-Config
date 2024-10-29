import json, binascii
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def readFile(file):
    with open(file, 'rt') as file:
        data = file.read()
        return data

def writeFile(file, data):
    with open(file, 'w') as file:
        file.write(data.hex())

def isDict(string):
    try:
        result = json.loads(string)
        return isinstance(result, dict)
    except ValueError:
        return False

def toBytes(hexStr):
    return binascii.unhexlify(hexStr)

def toJson(string):
    return json.loads(string)

def encrypt(string, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(string, AES.block_size))
    return encrypted

def decrypt(encryptedText, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encryptedText), AES.block_size)
    return decrypted.decode()
