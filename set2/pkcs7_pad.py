def pkcs7_pad(plaintext, block_size):
    pad_len = block_size - len(plaintext) % block_size
    padding = (chr(pad_len) * pad_len).encode()
    return plaintext + padding


def pkcs7_unpad(plaintext):
    pad_byte = plaintext[-1]
    if plaintext.endswith(chr(pad_byte).encode() * pad_byte):
        return plaintext[:-pad_byte]
    else:
        raise ValueError("Invalid padding")
