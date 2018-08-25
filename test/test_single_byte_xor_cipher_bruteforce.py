from unittest import TestCase

from set1.single_byte_xor_cipher_bruteforce import single_byte_xor_cipher_bruteforce


class TestSingleByteXorCipherBruteforce(TestCase):
    def test_single_byte_xor_cipher_bruteforce(self):
        self.assertEqual("Cooking MC's like a pound of bacon",
                         single_byte_xor_cipher_bruteforce(
                             "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")[2])
