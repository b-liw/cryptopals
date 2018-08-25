from unittest import TestCase

from set2.pkcs7_pad import pkcs7_pad


class TestPkcs7Pad(TestCase):
    def test_pkcs7_pad(self):
        self.assertEqual(b"YELLOW SUBMARINE\x04\x04\x04\x04", pkcs7_pad(b"YELLOW SUBMARINE", 20))
        self.assertEqual(b"\x10" * 16, pkcs7_pad(b"", 16))
        self.assertEqual(b"YELLOW SUBMARINE" + b"\x10" * 16, pkcs7_pad(b"YELLOW SUBMARINE", 16))
