from unittest import TestCase
from set1.detect_single_character_xor import *


class TestDetect_single_character_xor(TestCase):
    def test_detect_single_character_xor(self):
        with open("../res/4.txt", "r") as f:
            g = detect_single_character_xor(f.readlines())[2]
            self.assertEqual('Now that the party is jumping\n', g)
