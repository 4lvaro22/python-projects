from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto import Random

def initialize():
    _key = Random.get_random_bytes(16)
    _iv = Random.get_random_bytes(16)
    aes = AES.new(_key, AES.MODE_CBC, _iv)
    return aes

def cypher_text(aes):
    text = input("What message do you want to encrypt?\n").encode("utf-8")
    encrypt_text = aes.encrypt(pad(text, block_size=16))
    return encrypt_text

if __name__ == "__main__":
    aes = initialize()
    encrypt_text = cypher_text(aes)    
    print("Encrypted text: ")
    print(encrypt_text)
