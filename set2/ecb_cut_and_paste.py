from Crypto.Random import get_random_bytes
from Crypto.Random import random

from set2.aes_ecb import *
from set2.pkcs7_pad import *

block_size = 16
global_aes_128_key = get_random_bytes(block_size)


class User:
    def __init__(self, email, uid, role):
        self.email = email
        self.uid = uid
        self.role = role

    def encode_as_cookie(self):
        return "email={}&uid={}&role={}".format(self.email, self.uid, self.role)

    def is_admin(self):
        return self.role == "admin"

    def __str__(self):
        return "{{email: '{}', uid: {}, role: '{}'}}".format(self.email, self.uid, self.role)


def profile_for(email):
    email = email.replace("&", "")
    email = email.replace("=", "")
    return encrypt_encoded_user_cookie(User(email, random.randint(10, 99), "user"))


def decrypt_encoded_user_cookie(encrypted_cookie):
    cookie = decrypt_aes_128_ecb(encrypted_cookie, global_aes_128_key)
    cookie = pkcs7_unpad(cookie).decode()
    d = dict()
    for key_value in cookie.split("&"):
        key, value = key_value.split("=")
        d[key] = value
    email = d['email']
    uid = d['uid']
    role = d['role']
    return User(email, uid, role)


def encrypt_encoded_user_cookie(user):
    return encrypt_aes_128_ecb(pkcs7_pad(user.encode_as_cookie().encode(), block_size), global_aes_128_key)


def generate_payload_first_step():
    payload = ""
    payload += "A" * (block_size - len("email="))
    payload += "A" * (block_size - len("&uid=13&role="))
    return payload


def generate_payload_second_step():
    payload = ""
    payload += "A" * (block_size - len("email="))
    payload += pkcs7_pad(b"admin", block_size).decode()
    return payload


def ecb_cut_and_paste_attack():
    encrypted_cookie = profile_for(generate_payload_first_step())
    c1_12 = encrypted_cookie[0:32]
    encrypted_cookie2 = profile_for(generate_payload_second_step())
    c2_2 = encrypted_cookie2[16:32]
    cookie = c1_12 + c2_2
    user = decrypt_encoded_user_cookie(cookie)
    return user
