base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
pad_char = "="


def hex_to_base64(hex_str):
    out_str = ""
    for i in range(0, len(hex_str), 6):
        next_three_chars_hex_enc = hex_str[i:i + 6]
        num_of_chars_in_block = len(next_three_chars_hex_enc) // 2
        pad_len = 3 - (num_of_chars_in_block % 3)
        if pad_len == 3:
            pad_len = 0
        next_block = int(bin(int(next_three_chars_hex_enc, 16))[2:] + "00000000" * pad_len, 2)
        j = 3
        while j >= pad_len:
            a = (next_block >> (6 * j)) & 63
            j -= 1
            out_str += base64_alphabet[a]
        out_str += pad_char * pad_len
    return out_str
