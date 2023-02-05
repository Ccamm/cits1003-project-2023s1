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

##
# The Public Key and Ciphertext for this challenge
##
n = 308593594778211971013607578898980560251160874206358466697552377542456574663560413932906182507886825950148849588648239113295387893241582175146274623812305681332522693938542187038498509908127608858694023591666991726959096004420097914497460847800336647421256863401560682375054455580298602776427964943396596027274
e = 65537
ct = 126110251422950828560891656484477509850786177209042720207421968948693722211826777830813084916541800559375643187588955992235167396891145795103800669814074462154250967400264881040152300137185872507058248726088983467961466880034324020917244075818555389614695575725872588018246110133032582937874920457390086871127

##
# Task 1:
#   Figure out calculating the two primes that were used to generate the RSA public and private keys
##

# p = ?
# q = ?

n = p * q

##
# Task 2:
#   Using the given public key `e`, derive the private key `d` by using the prime numbers you discover in
#   task 1.
#
# Hint:
#   The adelie penguin might of done this part correctly.
##

# d = ?


# If you did task 1 and 2 correctly, this code will decrypt the ciphertext and print the flag.
flag_int = pow(ct, d, n)
print(f"flag: {long_to_bytes(flag_int).decode()}")