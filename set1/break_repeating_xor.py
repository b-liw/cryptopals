import binascii

from set1.single_byte_xor_cipher_bruteforce import single_byte_xor_cipher_bruteforce


def count_set_bits(num):
    count = 0
    while (num):
        count += num & 1
        num >>= 1
    return count


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have equal length")
    dist = 0
    for c1, c2 in zip(s1, s2):
        c1 = ord(c1)
        c2 = ord(c2)
        dist += count_set_bits(c1 ^ c2)
    return dist


def find_key_length(xored_msg):
    key = 0
    minimum_distance = 2 ** 32
    for key_size in range(2, 40):
        i = 3
        current_distance = hamming_distance(xored_msg[:key_size * i].decode(),
                                            xored_msg[key_size * i:key_size * i * 2].decode()) / float(key_size)
        if current_distance < minimum_distance:
            minimum_distance = current_distance
            key = key_size
    return key


def break_repeating_xor(xored_msg):
    key_length = find_key_length(xored_msg)
    key_size_length_blocks = [xored_msg[i:len(xored_msg):key_length] for i in range(0, key_length)]
    key = []
    for block in key_size_length_blocks:
        next_key_byte = single_byte_xor_cipher_bruteforce(binascii.hexlify(block).decode())
        key.append(next_key_byte[1])
    key_str = "".join(map(chr, key))
    # print(key_str)
    # print(binascii.unhexlify(repeating_xor(xored_msg.decode(), key_str)).decode())

    return key_str
