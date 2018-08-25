from unittest import TestCase

from set1.detect_aes_in_ecb_mode import detect_single_aes_in_ecb_mode
from set2.ecb_cbc_detection_oracle import cbc_ecb_oracle


class TestEcbCbcDetectionOracle(TestCase):
    def test_ecb_cbc_detection_oracle(self):
        payload = b"A" * 50
        ecb = 0
        cbc = 0
        for i in range(500):
            ciphertext = cbc_ecb_oracle(payload)
            if detect_single_aes_in_ecb_mode(ciphertext):
                ecb += 1
            else:
                cbc += 1
        self.assertAlmostEqual(ecb, cbc, delta=50)
