from unittest import TestCase

from set1.hex_to_base64 import hex_to_base64


class TestHexToBase64(TestCase):
    def test_hex_to_base64(self):
        self.assertEqual("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t", hex_to_base64(
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"))
        self.assertEqual("YW55IGNhcm5hbCBwbGVhc3Vy", hex_to_base64("616e79206361726e616c20706c6561737572"))
        self.assertEqual("YW55IGNhcm5hbCBwbGVhcw==", hex_to_base64("616e79206361726e616c20706c656173"))
