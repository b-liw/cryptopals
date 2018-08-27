import base64

from Crypto.Random import get_random_bytes

from set2.aes_ecb import encrypt_aes_128_ecb
from set2.pkcs7_pad import pkcs7_pad

oracle_global_key = get_random_bytes(16)


def brute_force_block_size(ciphertext):
    for block_size in range(2, 64):
        if len(ciphertext) % block_size == 0:
            blocks = [ciphertext[i * block_size:i * block_size + block_size] for i in
                      range(0, len(ciphertext) // block_size)]
            for i in range(len(blocks) - 1):
                if blocks[i] == blocks[i + 1]:
                    return block_size
    return None


def ecb_suffix_oracle(plaintext):
    random_prefix = b"tEOW49TgR2bg7HRhJdFLpjAXX7Ju6iZgxJRbyUdvoWQAETI1Gt5x5Gyp47rjZw"
    secret_suffix = base64.b64decode(
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    return encrypt_aes_128_ecb(pkcs7_pad(random_prefix + plaintext + secret_suffix, 16), oracle_global_key)


def get_block_size():
    ciphertext = ecb_suffix_oracle(b"A" * 100)
    return brute_force_block_size(ciphertext)


b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00'


def get_offset_and_pad_count_of_prefix(block_size):
    for pad_count in range(1, block_size + 1):
        pad_to_align_prefix_to_block_size = b"B" * pad_count
        ciphertext = ecb_suffix_oracle(pad_to_align_prefix_to_block_size + b"A" * block_size * 2)
        blocks = [ciphertext[i * block_size:i * block_size + block_size] for i in
                  range(0, len(ciphertext) // block_size)]
        for i in range(0, len(blocks) - 1):
            if blocks[i] == blocks[i + 1]:
                return pad_count, i * block_size
    return None


def break_ecb_suffix_oracle_harder():
    retrieved_secret = b""
    try:
        block_size = get_block_size()
        pad_count, offset = get_offset_and_pad_count_of_prefix(block_size)
        num_of_blocks = 10
        for n in range(1, num_of_blocks * block_size):
            encrypt_dict = dict()
            prefix_template = b"B" * pad_count + b"A" * ((block_size * num_of_blocks) - n)
            for unknown_byte in range(0, 256):
                prefix = prefix_template + retrieved_secret + chr(unknown_byte).encode()
                k = ecb_suffix_oracle(prefix)
                encrypt_dict[k[offset:offset + block_size * num_of_blocks]] = unknown_byte
            retrieved_secret += chr(
                encrypt_dict[ecb_suffix_oracle(prefix_template)[offset:offset + block_size * num_of_blocks]]).encode()
    except ValueError:
        return retrieved_secret
    finally:
        return retrieved_secret
