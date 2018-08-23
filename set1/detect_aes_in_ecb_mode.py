def detect_aes_in_ecb_mode(ciphertexts):
    block_size = 16
    for cipher in ciphertexts:
        cipher = cipher.strip()
        blocks_set = set()
        blocks = [cipher[i*block_size:i*block_size+block_size] for i in range(0, len(cipher) // block_size)]
        for block in blocks:
            blocks_set.add(block)
        if len(blocks_set) != len(blocks):
            return cipher