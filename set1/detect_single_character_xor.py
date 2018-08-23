from set1.single_byte_xor_cipher_bruteforce import *


def detect_single_character_xor(l):
    out = []
    for s in l:
        out.append(single_byte_xor_cipher_bruteforce(s.strip()))
    return sorted(out, key=lambda k: k[0], reverse=True)[0]
