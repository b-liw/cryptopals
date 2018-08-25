import base64
from unittest import TestCase

from set1.break_repeating_xor import *


class TestBreakRepeatingXor(TestCase):
    def test_hamming_distance(self):
        self.assertEqual(37, hamming_distance("this is a test", "wokka wokka!!!"))

    def test_break_repeating_xor(self):
        base64_encoded_msg = ""
        with open("../res/6.txt", "r") as f:
            for line in f.readlines():
                base64_encoded_msg += line.strip()
        xored_msg = base64.b64decode(base64_encoded_msg)
        self.assertEqual("Terminator X: Bring the noise", break_repeating_xor(xored_msg))
