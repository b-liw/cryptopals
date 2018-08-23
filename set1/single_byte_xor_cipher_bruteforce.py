import binascii
import string

NOT_ENGLISH_TEXT = 9999

english_freq = [
    0.0651738, 0.0124248, 0.0217339, 0.0349835,  # 'A', 'B', 'C', 'D'
    0.1041442, 0.0197881, 0.0158610, 0.0492888,
    0.0558094, 0.0009033, 0.0050529, 0.0331490,
    0.0202124, 0.0564513, 0.0596302, 0.0137645,
    0.0008606, 0.0497563, 0.0515760, 0.0729357,
    0.0225134, 0.0082903, 0.0171272, 0.0013692,
    0.0145984, 0.0007836, 0.1918182  # 'Y', 'Z', ' '
]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
frequency_map_keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


def get_ascii_char_frequency(text):
    char_freq_map = dict()
    for key in frequency_map_keys:
        char_freq_map[key] = 0
    for c in text:
        if c in alphabet:
            c = c.upper()
            char_freq_map[c] += 1
    return char_freq_map


def chi_square_test(char_frequency):
    length = 0
    sum = 0
    for key in char_frequency:
        length += char_frequency[key]
    for c in frequency_map_keys:
        observed = char_frequency[c]
        if c == ' ':
            k = 26
        else:
            k = ord(c) - ord('A')
        expected = length * english_freq[k]
        diff = observed - expected
        sum += (diff * diff) / float(expected)
    return sum


def frequency_test(char_frequency):
    sum = 0
    for key in char_frequency:
        if key == ' ':
            k = 26
        else:
            k = ord(key) - ord('A')
        sum += english_freq[k] * char_frequency[key]
    return sum


def is_string_printable(s):
    for c in s:
        if c not in string.printable:
            return False
    return True


def score_english_text(text):
    return frequency_test(get_ascii_char_frequency(text))


def single_byte_xor_cipher_bruteforce(hex_enc_str):
    bytes_from_hex_enc_str = binascii.unhexlify(hex_enc_str)
    out = []
    for key in range(0xFF):
        out.append((key, "".join([chr(c ^ key) for c in bytes_from_hex_enc_str])))
    possible_decrypted_texts = sorted(list(map(lambda k: (score_english_text(k[1]), k[0], k[1]), out)), key=lambda k: k[0], reverse=True)
    return possible_decrypted_texts[0]
