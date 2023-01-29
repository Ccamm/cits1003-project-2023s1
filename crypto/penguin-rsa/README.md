# Challenge

**Name:** Penguin RSA

**Category:** Cryptography

**Difficulty:** Hard

**Flag:** `UWA{mAyB3_i_sH0vLd_sT0p_3aTn_f15h_Nd_k33p_mI_pR1m35_s3CvRe!!one!}`

---

## Description

An adélie penguin came waddling over to you excitedly holding a toshiba laptop. On the laptop they showed some `python` code that they wrote that implemented the RSA asymmetric encryption algorithm *securely* and *two times faster than other implementations*. The penguin then sent you file named `out.txt` that contained the RSA public key (`n`, `e`) and an encrypted flag (`ct`). The penguin and then stared deep into your eyes and said while flapping their wings excitedly:

> waa waa wa wa wa

Which translated to:

> Can you decrypt my message that I encrypted using my RSA algorithm?

To help solve this challenge, you will need to write a small python program to solve this challenge (you can adapt the code provided in `penguinrsa.py`). It is highly recommended to copy the following `long_to_bytes` function that converts numbers into bytes for printing the flag.


```python
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
```

In addition, to help solve this challenge the RSA key generation is explained below:

1. Pick to random prime numbers called `p` and `q` (*keep these secure*).
2. Calculate `n = p x q`.
3. Calculate the Euler totient `phi = (p-1) x (q-1)`.
4. Choose a public key `e`. There are mathematical properties that need to be satisfied when choosing `e`, but for simplicity setting the public key `e = 65537` is fine.
5. Calculate the private key `d` (the modular inverse of the public key with the euler totient `d = pow(e, -1, phi)`).
6. Encrypt the message `pt` using the public key `e` (`ct = pow(pt, e, n)`).
7. Decrypt the encrypted message `ct` using the private key `d` (`pt = pow(ct, d, n)`).

---

## Solution

Reading the provided code, we can see that one of the prime numbers for generating the RSA keys is set to **`2`**. Since we know one of the primes, we can calculate the randomly generated prime using **`n / 2`**! Then we just copy the RSA process for generating the private key and decrypting the flag.

*solution code*
```python
from Crypto.Util.number import long_to_bytes
from binascii import unhexlify

def long_to_bytes (val, endianness='big'):
    width = val.bit_length()
    width += 8 - ((width % 8) or 8)
    fmt = '%%0%dx' % (width // 4)
    s = unhexlify(fmt % val)

    if endianness == 'little':
        s = s[::-1]

    return s

n = 308593594778211971013607578898980560251160874206358466697552377542456574663560413932906182507886825950148849588648239113295387893241582175146274623812305681332522693938542187038498509908127608858694023591666991726959096004420097914497460847800336647421256863401560682375054455580298602776427964943396596027274
e = 65537
ct = 126110251422950828560891656484477509850786177209042720207421968948693722211826777830813084916541800559375643187588955992235167396891145795103800669814074462154250967400264881040152300137185872507058248726088983467961466880034324020917244075818555389614695575725872588018246110133032582937874920457390086871127

# We know that 2 is one of the primes, we can derive the other prime easily
q = 2
p = n // q

# Since we have both primes, we can derive the euler totient and determine the private key
phi = (p-1) * (q-1)
d = pow(e, -1, phi)

flag_int = pow(ct, d, n)
print(f"flag: {long_to_bytes(flag_int).decode()}")
```