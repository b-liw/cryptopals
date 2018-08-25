import binascii

from set2.aes_ecb import decrypt_aes_128_ecb
from set2.aes_ecb import encrypt_aes_128_ecb


def decrypt_aes_cbc(iv, ciphertext, key, block_size=16):
    if len(ciphertext) % block_size != 0:
        raise ValueError("plaintext length is incorrect")
    decrypted_blocks = []
    encrypted_blocks = list(reversed(
        [iv] + [ciphertext[i * block_size:i * block_size + block_size] for i in range(len(ciphertext) // block_size)]))
    for i in range(len(encrypted_blocks) - 1):
        block = encrypted_blocks[i]
        intermediate_block = decrypt_aes_128_ecb(block, key)
        plain_text_block = int(binascii.hexlify(intermediate_block), 16) ^ int(
            binascii.hexlify(encrypted_blocks[i + 1]), 16)
        decrypted_blocks.append(binascii.unhexlify(hex(plain_text_block)[2:].rjust(block_size * 2, "0")))
    return b"".join(reversed(decrypted_blocks))


def encrypt_aes_cbc(iv, plaintext, key, block_size=16):
    if len(plaintext) % block_size != 0:
        raise ValueError("plaintext length is incorrect")
    encrypted_blocks = [iv]
    blocks = list([plaintext[i * block_size:i * block_size + block_size] for i in range(len(plaintext) // block_size)])
    for i in range(0, len(blocks)):
        block = blocks[i]
        intermediate_block = int(binascii.hexlify(block), 16) ^ int(binascii.hexlify(encrypted_blocks[i]), 16)
        cipher_block = encrypt_aes_128_ecb(binascii.unhexlify(hex(intermediate_block)[2:].rjust(block_size * 2, "0")),
                                           key)
        encrypted_blocks.append(cipher_block)
    return b"".join(encrypted_blocks[1:])
