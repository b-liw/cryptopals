from Crypto.Random import get_random_bytes
from Crypto.Random import random

from set2.aes_cbc import encrypt_aes_cbc
from set2.aes_ecb import encrypt_aes_128_ecb
from set2.pkcs7_pad import pkcs7_pad


def cbc_ecb_oracle(plaintext):
    prefix_len = random.randint(5, 10)
    suffix_len = random.randint(5, 10)
    plaintext = get_random_bytes(prefix_len) + plaintext + get_random_bytes(suffix_len)
    key = get_random_bytes(16)
    if random.randint(0, 1):
        return encrypt_aes_cbc(get_random_bytes(16), pkcs7_pad(plaintext, 16), key)
    else:
        return encrypt_aes_128_ecb(pkcs7_pad(plaintext, 16), key)
