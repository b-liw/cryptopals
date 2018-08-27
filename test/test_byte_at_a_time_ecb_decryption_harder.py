from unittest import TestCase

from set2.byte_at_a_time_ecb_decryption_harder import *


class TestByteAtATimeEcbDecryptionHarder(TestCase):
    def test_ecb_suffix_oracle(self):
        self.assertTrue(break_ecb_suffix_oracle_harder().decode().startswith("Rollin"))
