plainText = input()
key = input()


def encrypt():
    cipher_ = [(ord(a)-ord('A')) ^ (ord(b)-ord('A'))
               for a, b in zip(plainText, key)]
    cipher = [chr(i % 26 + ord('A')) for i in cipher_]
    return cipher, cipher_

cipher, cipher_ = encrypt()
print("".join(cipher))


def decrypt():
    text_ = [a ^ (ord(b)-ord('A'))
             for a, b in zip(cipher_, key)]
    text = [chr(i % 26 + ord('A')) for i in text_]
    return text, text_

text, text_ = decrypt()
print("".join(text))
