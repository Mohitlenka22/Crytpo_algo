# Caesar cipher
# key = int(input())
# plainText = input()

# def f(text, key):
#     new = ''
#     for i in text:
#         if i == ' ':
#             new += i
#         else:
#             if i.isdigit():
#                 new += chr((ord(i) - ord('0') + key) % 10 + ord('0'))
#             elif ord(i) in range(65, 91):
#                 new += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
#             elif ord(i) in range(97, 123):
#                 new += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
#             else:
#                 new += chr((ord(i) + key) % 128)
#     return new

# def encryption(plainText, key):
#     return f(plainText, key)

# def decryption(cipherText, key):
#     return f(cipherText, key)

# en = encryption(plainText, key)
# print(en.upper())
# de = decryption(en, -key)
# print(de)
# # PHHW PH DIWHU 6SP CJYS


#  Hill cipher

# from math import sqrt
# import numpy as np
# from sympy import Matrix

# plainText = input()
# key = input()

# kylen = len(key)
# ptlen = len(plainText)

# ky_dim = int(sqrt(kylen))

# plainText_mt = np.array([ord(i)-ord('A') for i in plainText])
# plainText_mt = plainText_mt.reshape(ptlen//ky_dim, ky_dim)

# key_mt = np.array([ord(i) - ord('A') for i in key])
# key_mt = key_mt.reshape(ky_dim, ky_dim)

# def encrypt():
#     cipher = np.array([])
#     for i in range(ptlen//ky_dim):
#         row = np.matmul(key_mt, plainText_mt[i])
#         cipher = np.append(cipher, list(map(chr, row % 26 + ord('A'))))
#     return cipher

# cipher_ = encrypt()
# cipher = "".join(cipher_)
# print(cipher)

# cipher_mt = np.array([ord(i)-ord('A') for i in cipher])
# cipher_mt = cipher_mt.reshape(ptlen//ky_dim, ky_dim)

# def decrypt():
#     A = Matrix(key_mt)
#     key_mt_inv = A.inv_mod(26)
#     text = np.array([])
#     for i in range(ptlen//ky_dim):
#         row = np.matmul(key_mt_inv, cipher_mt[i])
#         text = np.append(text, list(map(chr, row % 26 + ord('A'))))
#     return text

# text = decrypt()
# print("".join(text))

# # LNSHDLEWMTRW


# Simple des

# IP = [2, 6, 3, 1, 4, 8, 5, 7]
# EP = [4, 1, 2, 3, 2, 3, 4, 1]
# IP_INVERSE = [4, 1, 3, 5, 7, 2, 8, 6]
# P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
# P8 = [6, 3, 7, 4, 8, 5, 10, 9]
# P4 = [2, 4, 3, 1]

# S0 = [[1, 0, 3, 2],
#       [3, 2, 1, 0],
#       [0, 2, 1, 3],
#       [3, 1, 3, 2]]

# S1 = [[0, 1, 2, 3],
#       [2, 0, 1, 3],
#       [3, 0, 1, 0],
#       [2, 1, 0, 3]]


# def permutate(original, fixed_key):
#     new = ''
#     for i in fixed_key:
#         new += original[i-1]
#     return new


# def lefthalf(bits):
#     return bits[:len(bits)//2]


# def righthalf(bits):
#     return bits[len(bits)//2:]


# def shift(bits):
#     rotated_left_half = lefthalf(bits)[1:] + lefthalf(bits)[0]
#     rotated_right_half = righthalf(bits)[1:] + righthalf(bits)[0]
#     return rotated_left_half + rotated_right_half


# def key1():
#     return permutate(shift(permutate(KEY, P10)), P8)


# def key2():
#     return permutate(shift(shift(shift(permutate(KEY, P10)))), P8)


# def xor(bits, key):
#     new = ''
#     for bit, key_bit in zip(bits, key):
#         new += str((int(bit)+int(key_bit)) % 2)
#     return new


# def lookup_in_sbox(bits, sbox):
#     row = int(bits[0] + bits[3], 2)
#     col = int(bits[1] + bits[2], 2)
#     return '{0:02b}'.format(sbox[row][col])


# def f_k(bits, key):
#     L = lefthalf(bits)
#     R = righthalf(bits)
#     bits = permutate(R, EP)
#     bits = xor(bits, key)
#     temp = lookup_in_sbox(lefthalf(bits), S0) + lookup_in_sbox(righthalf(bits), S1)
#     temp = permutate(temp, P4)
#     return xor(L, temp)

# def encrypt(plain_text):
#     bits = permutate(plain_text, IP)
#     temp = f_k(bits, key1())
#     bits = righthalf(bits) + temp
#     bits = f_k(bits, key2())
#     print(permutate(bits + temp, IP_INVERSE))
#     return permutate(bits + temp, IP_INVERSE)


# def decrypt(cipher_text):
#     bits = permutate(cipher_text, IP)
#     temp = f_k(bits, key2())
#     bits = righthalf(bits) + temp
#     bits = f_k(bits, key1())
#     print(permutate(bits + temp, IP_INVERSE))


# KEY = input("Enter key: ")
# cipher = encrypt(input("Enter Plain text: "))
# decrypt(cipher)


# rsa

# def isprime(n):
#     if n == 1 or n == 2:
#         return n == 2
#     for i in range(2, n**(1/2)+1):
#         if n % i != 0:
#             return False
#     return True


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# def generate_keypair(p, q):
#     n = p * q
#     phi = (p-1) * (q-1)
#     e = 65537 # 2
#     # while gcd(e, phi) != 1:
#     #     e += 1
#     d = pow(e, -1, phi)
#     return ((e, n), (d, n))


# def encrypt(pt, public_key):
#     e, n = public_key
#     cipher = [pow(ord(i), e, n) for i in pt]
#     return cipher


# def decrypt(cipher, private_key):
#     d, n = private_key
#     text = [pow(ord(i), d, n) for i in cipher]
#     return text


# p = int(input())
# q = int(input())
# pt = input()

# public_key, private_key = generate_keypair(p, q)
# cp = encrypt(pt, public_key)
# cp = [chr(i) for i in cp]
# print("".join(cp))
# tt = decrypt("".join(cp), private_key)
# tt = [chr(i) for i in tt]
# print("".join(tt))


# hellman

# def hellman():
#     p = int(input())
#     g = int(input())
#     a = int(input())
#     b = int(input())

#     # public_keys
#     A = pow(g, a, p)
#     B = pow(g, b, p)

#     print("A Sent to B : ", A)
#     print("B Sent to A : ", B)

#     k1 = pow(B, a, p)
#     k2 = pow(A, b, p)

#     print("Shared secret key for A:", k1)
#     print("Shared secret key for B:", k2)

# hellman()


# rail fence

# plainText = input()
# key = int(input())


# def encrypt(plainText, key):
#     cipher = ""

#     row = key
#     col = len(plainText)
#     check = False
#     j = 0
#     a = [[' ' for i in range(col)] for i in range(row)]
#     for i in range(len(plainText)):
#         if j == 0 or j == key-1:
#             check = not check
#         a[j][i] = plainText[i]

#         if check:
#             j += 1
#         else:
#             j -= 1

#     for i in range(row):
#         for j in range(col):
#             if a[i][j] != ' ':
#                 cipher += a[i][j]
#     return cipher


# def decrypt(cipher, key):
#     text = ""

#     row = key
#     col = len(plainText)
#     check = False
#     j = 0
#     a = [[' ' for i in range(col)] for i in range(row)]
#     for i in range(len(cipher)):
#         if j == 0 or j == key-1:
#             check = not check
#         a[j][i] = '*'
#         if check:
#             j += 1
#         else:
#             j -= 1

#     index = 0
#     for i in range(row):
#         for j in range(col):
#             if a[i][j] == '*' and index < col:
#                 a[i][j] = cipher[index]
#                 index += 1

#     j = 0
#     check = False
#     for i in range(len(cipher)):
#         if j == 0 or j == key-1:
#             check = not check
#         text += a[j][i]
#         if check:
#             j += 1
#         else:
#             j -= 1

#     return text


# en = encrypt(plainText, key)
# print(en)
# t = decrypt(en, key)
# print(t)


# row column transposition

# import math


# def encrypt(msg):
#     col = len(key)
#     row = int(math.ceil(len(msg)/col))
#     fill_null = row*col - len(msg)
#     msg += '_'*fill_null

#     matrix = [msg[i:i+col] for i in range(0, len(msg), col)]
#     cipher = ''.join([matrix[i][key.index(k)]
#                      for k in sorted(key) for i in range(row)])
#     return cipher


# def decrypt(msg):
#     col = len(key)
#     row = int(math.ceil(len(msg)/col))
#     matrix = [[''] * col for i in range(row)]
#     key_sorted = sorted(key)
#     index = 0
#     for k in key_sorted:
#         col = key.index(k)
#         for j in range(row):
#             matrix[j][col] = msg[index]
#             index += 1
#     text = ''.join(''.join(row) for row in matrix).rstrip('_')
#     return text


# msg = "mohitlenka"
# key = "HACK"

# en = encrypt(msg)
# print(en)

# t = decrypt(en)
# print(t)

#  Miller rabin

