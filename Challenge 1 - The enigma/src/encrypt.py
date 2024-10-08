from Crypto.Cipher import ChaCha20
import random

randkey = random.randbytes(32)
nonce = random.randbytes(8)

def encrypt_and_update(msg, nonce):
    cipher = ChaCha20.new(key=randkey, nonce=nonce)
    nonce = random.getrandbits(12*8)
    return cipher.encrypt(msg.encode())

with open('message.txt', 'r') as m:
    for line in m:
        print(encrypt_and_update(line, nonce).hex())
