from unittest import TestCase

from set2.cbc_bitflipping_attack import *


class TestCbcBitflippingAttack(TestCase):
    def test_cbc_bitflipping_attack(self):
        block_size = 16
        key = get_random_bytes(block_size)
        iv = get_random_bytes(block_size)
        ciphertext = encrypt_user_data(insert_user_data_into_dummy_string("?admin?true").encode(), key, iv)
        blocks = [ciphertext[i * block_size:i * block_size + block_size] for i in range(len(ciphertext) // block_size)]
        c1 = list(blocks[1])
        c1[0] ^= ord("?") ^ ord(";")
        c1[6] ^= ord("?") ^ ord("=")
        blocks[1] = bytes(c1)
        new_ciphertext = b"".join(blocks)
        plaintext = decrypt_user_data(new_ciphertext, key, iv)
        self.assertTrue(is_admin(plaintext))
