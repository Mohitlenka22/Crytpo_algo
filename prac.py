# from math import sqrt
# import numpy as np
# from sympy import Matrix

# plainText = input()
# key = input()

# ptlen = len(plainText)
# kylen = len(key)

# kydim = int(sqrt(kylen))


# key_matrix = np.array([ord(i)-ord('A') for i in key])
# key_matrix = key_matrix.reshape(kydim, kydim)

# pt_matrix = np.array([ord(i)-ord('A') for i in plainText])
# pt_matrix = pt_matrix.reshape(ptlen//kydim, kydim)


# def encrypt():
#     cipher_matrix = np.array([])
#     for i in range(ptlen//kydim):
#         row = np.matmul(key_matrix, pt_matrix[i])
#         cipher_matrix = np.append(
#             cipher_matrix, list(map(chr, row % 26 + ord('A'))))
#     return cipher_matrix


# cipher_matrix = encrypt()
# cipher = "".join(cipher_matrix)
# print("cipher: ", cipher)

# cipher_matrix = np.array([ord(i)-ord('A') for i in cipher])
# cipher_matrix = cipher_matrix.reshape(ptlen//kydim, kydim)


# def decrypt():
#     A = Matrix(key_matrix)
#     key_matrix_inv = A.inv_mod(26)
#     plainText_matrix = np.array([])
#     for i in range(ptlen//kydim):
#         row = np.matmul(key_matrix_inv, cipher_matrix[i])
#         plainText_matrix = np.append(
#             plainText_matrix, list(map(chr, row % 26 + ord('A'))))
#     return plainText_matrix


# plainText_matrix = decrypt()
# print("pt: ", "".join(plainText_matrix))


