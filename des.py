IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4 = [2, 4, 3, 1]

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

S1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]


def permutate(original, key):
    newkey = ''
    for i in key:
        newkey += original[i - 1]
    return newkey


def left_half(bits):
    return bits[:len(bits)//2]


def right_half(bits):
    return bits[len(bits)//2:]


def shift(bits):
    rotated_left_half = left_half(bits)[1:] + left_half(bits)[0]
    rotated_right_half = right_half(bits)[1:] + right_half(bits)[0]
    return rotated_left_half + rotated_right_half


def key1():
    return permutate(shift(permutate(KEY, P10)), P8)


def key2():
    return permutate(shift(shift(shift(permutate(KEY, P10)))), P8)


def xor(bits, key):
    new = ''
    for bit, key_bit in zip(bits, key):
        new += str(((int(bit) + int(key_bit)) % 2))
    return new


def lookup_in_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])


def f_k(bits, key):
    L = left_half(bits)
    R = right_half(bits)
    bits = permutate(R, EP)
    bits = xor(bits, key)
    bits = lookup_in_sbox(left_half(bits), S0) + lookup_in_sbox(right_half(bits), S1)
    bits = permutate(bits, P4)
    return xor(bits, L)


def encrypt(plain_text):
    bits = permutate(plain_text, IP)
    temp = f_k(bits, key1())
    # swap
    bits = right_half(bits) + temp
    bits = f_k(bits, key2())
    print("Cipher Text: ", permutate(bits + temp, IP_INVERSE))
    return permutate(bits + temp, IP_INVERSE)


def decrypt(cipher_text):
    bits = permutate(cipher_text, IP)
    temp = f_k(bits, key2())
    bits = right_half(bits) + temp
    bits = f_k(bits, key1())
    print("Original Message: ", permutate(bits + temp, IP_INVERSE))


KEY = input("Enter key: ")
cipher = encrypt(input("Enter Plain text: "))
decrypt(cipher)
