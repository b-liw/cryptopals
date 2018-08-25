def detect_aes_in_ecb_mode(ciphertexts, block_size=16):
    for ciphertext in ciphertexts:
        if detect_single_aes_in_ecb_mode(ciphertext, block_size):
            return ciphertext
    return False


def detect_single_aes_in_ecb_mode(ciphertext, block_size=16):
    blocks_set = set()
    blocks = [ciphertext[i * block_size:i * block_size + block_size] for i in range(0, len(ciphertext) // block_size)]
    for block in blocks:
        blocks_set.add(block)
    return len(blocks_set) != len(blocks)
