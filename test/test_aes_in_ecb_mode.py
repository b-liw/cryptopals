from unittest import TestCase

from set1.aes_in_ecb_mode import aes_in_ecb_mode
import base64

class TestBreak_repeating_xor(TestCase):

    def test_aes_in_ecb_mode(self):
        base64_encoded_msg = ""
        with open("../res/7.txt", "r") as f:
            for line in f.readlines():
                base64_encoded_msg += line.strip()
        aes_ecb_b64_msg = base64.b64decode(base64_encoded_msg)
        self.assertTrue(aes_in_ecb_mode(aes_ecb_b64_msg, "YELLOW SUBMARINE").startswith("I'm back and I'm ringin' the bell"))
