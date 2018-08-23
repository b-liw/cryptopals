import binascii


def repeating_xor(text, key):
    len_of_key = len(key)
    out = []
    i = 0
    for c in text:
        out.append((ord(key[i % len_of_key]) ^ ord(c)) & 0xFF)
        i += 1
    return binascii.hexlify(bytes(out)).decode()
