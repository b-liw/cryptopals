from set2.aes_cbc import *
from set2.pkcs7_pad import *

block_size = 16


def insert_user_data_into_dummy_string(data):
    data = data.replace(";", "").replace("=", "")
    return "comment1=cooking%20MCs;userdata=" + data + ";comment2=%20like%20a%20pound%20of%20bacon"


def is_admin(data):
    return b";admin=true;" in data


def encrypt_user_data(plaintext, key, iv):
    return encrypt_aes_128_cbc(iv, pkcs7_pad(plaintext, block_size), key)


def decrypt_user_data(ciphertext, key, iv):
    return pkcs7_unpad(decrypt_aes_128_cbc(iv, ciphertext, key))
