from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from binascii import unhexlify

def encrypt_username(key: bytes, username: bytes) -> str:
    """
        Encrypts the username and creates an authentication cookie
    """
    # Generates a random IV for the authentication cookie
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    enc_username = cipher.encrypt(pad(username, AES.block_size))

    # Returns the authentication cookie in the format {IV}:{encrypted username}
    return f"{iv.hex()}:{enc_username.hex()}"


def decrypt_auth_cookie(key: bytes, auth_cookie: str) -> str:
    """
        Decrypts the authentication cookie and retrieves the user's username
    """
    # Splits the authentication cookie by ':' to get the IV and encrypted username
    iv_hex, enc_username_hex = auth_cookie.split(':')

    # Decodes the IV and encrypted username from hex
    iv = unhexlify(iv_hex)
    enc_username = unhexlify(enc_username_hex)

    # Decrypts the username field
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc_username), AES.block_size).decode()