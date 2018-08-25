from unittest import TestCase

from set1.fixed_xor import *


class TestFixedXor(TestCase):
    def test_fixed_xor(self):
        self.assertEqual("746865206b696420646f6e277420706c6179",
                         fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"))
