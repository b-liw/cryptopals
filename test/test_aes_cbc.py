from base64 import b64decode
from unittest import TestCase

from set2.aes_cbc import decrypt_aes_128_cbc, encrypt_aes_128_cbc


class TestAesCbc(TestCase):
    def test_aes_cbc(self):
        block_size = 16
        iv = (chr(0) * block_size).encode()
        with open("../res//10.txt", "r") as f:
            lines = f.readlines()
        ciphertext = b"".join([b64decode(line.strip()) for line in lines])
        plain_text = decrypt_aes_128_cbc(iv, ciphertext, "YELLOW SUBMARINE")
        self.assertTrue(plain_text.startswith(b"I'm back and"))
        ciphertext2 = encrypt_aes_128_cbc(iv, plain_text, "YELLOW SUBMARINE")
        self.assertTrue(ciphertext == ciphertext2)
