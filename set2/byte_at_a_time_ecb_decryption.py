import base64

from Crypto.Random import get_random_bytes

from set1.detect_aes_in_ecb_mode import detect_single_aes_in_ecb_mode
from set2.aes_ecb import encrypt_aes_128_ecb
from set2.pkcs7_pad import pkcs7_pad

oracle_global_key = get_random_bytes(16)


def detect_ecb_block_size_oracle():
    for block_size in range(1, 64 + 1):
        ciphertext = ecb_suffix_oracle(b"A" * block_size * 2)
        if detect_single_aes_in_ecb_mode(ciphertext):
            return block_size
    return 0


def ecb_suffix_oracle(plaintext):
    secret_suffix = base64.b64decode(
        "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK")
    return encrypt_aes_128_ecb(pkcs7_pad(plaintext + secret_suffix, 16), oracle_global_key)


def break_ecb_suffix_oracle():
    retrieved_secret = b""
    try:
        block_size = detect_ecb_block_size_oracle()
        num_of_blocks = 10
        for n in range(1, num_of_blocks * block_size):
            encrypt_dict = dict()
            prefix_template = b"A" * ((block_size * num_of_blocks) - n)
            for unknown_byte in range(0, 256):
                prefix = prefix_template + retrieved_secret + chr(unknown_byte).encode()
                k = ecb_suffix_oracle(prefix)
                encrypt_dict[k[:block_size * num_of_blocks]] = unknown_byte
            retrieved_secret += chr(
                encrypt_dict[ecb_suffix_oracle(prefix_template)[:block_size * num_of_blocks]]).encode()
    except ValueError:
        return retrieved_secret
    finally:
        return retrieved_secret
