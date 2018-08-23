from Crypto.Cipher import AES


def aes_in_ecb_mode(msg, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(msg).decode()
