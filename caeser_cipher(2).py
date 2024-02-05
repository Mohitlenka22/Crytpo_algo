def encryption(text, key):
    cipher = ""
    for i in text:
        if i == " ":
            cipher += " "
        else:
            if i.isdigit():
                cipher += chr(((ord(i)-ord('0')+key) % 10)+ord('0'))
            elif ord(i) in range(97, 123):
                cipher += chr(((ord(i)-ord('a')+key) % 26)+ord('a'))
            elif ord(i) in range(65, 91):
                cipher += chr(((ord(i)-ord('A')+key) % 26)+ord('A'))
            else:
                cipher += chr((ord(i)+key) % 128)
    return cipher


def decryption(cipher, key):
    text = ""
    for i in cipher:
        if i == " ":
            text += " "
        else:
            if i.isdigit():
                text += chr(((ord(i)-ord('0')-key) % 10)+ord('0'))
            elif ord(i) in range(97, 123):
                text += chr(((ord(i)-ord('a')-key) % 26)+ord('a'))
            elif ord(i) in range(65, 91):
                text += chr(((ord(i)-ord('A')-key) % 26)+ord('A'))
            else:
                text += chr((ord(i)-key) % 128)
    return text
    # text = encryption(cipher, -key)
    # return text


key = int(input("Enter Key: "))
cipher = encryption(input("Enter Plain text: "), key)
text = decryption(cipher, key)
print("Cipher Text: ", cipher.upper())
print("Plain Text: ",  text)

