def pkcs7_pad(plaintext, block_size):
    pad_len = block_size - len(plaintext) % block_size
    padding = (chr(pad_len) * pad_len).encode()
    return plaintext + padding


def pkcs7_unpad(plaintext):
    return plaintext[:-ord(plaintext[-1])]
