from Crypto.Util.number import bytes_to_long, getPrime
# Stolen from https://stackoverflow.com/questions/8730927/convert-python-long-int-to-fixed-size-byte-array
from binascii import unhexlify

def long_to_bytes(val, endianness='big'):
    width = val.bit_length()
    width += 8 - ((width % 8) or 8)
    fmt = '%%0%dx' % (width // 4)
    s = unhexlify(fmt % val)

    if endianness == 'little':
        s = s[::-1]

    return s

with open("flag.txt", "rb") as f:
    flag = bytes_to_long(f.read().strip())

# Generate prime numbers
p = getPrime(1024)
# Improve performance by just picking one of the primes as 2
q = 2

# Calculate n
n = p*q

# Choose a public key
e = 0x10001

# Calculate the Euler totient (don't worry if you do not understand, just note how it is done)
phi = (p-1) * (q-1)

# Derive the private key
d = pow(e, -1, phi)

# Encrypt the flag
ct = pow(flag, e, n)

# Save the message and the public key
with open("out.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"ct = {ct}\n")

# Test Penguin RSA works by decrypting the encrypted flag and printing
test_decrypted = pow(ct, d, n)
print(long_to_bytes(test_decrypted).decode())