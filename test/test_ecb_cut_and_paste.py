from unittest import TestCase
from set2.ecb_cut_and_paste import *


class TestEcbCutAndPaste(TestCase):
    def test_ecb_cut_and_paste(self):
        user = ecb_cut_and_paste_attack()
        self.assertTrue(user.is_admin())
