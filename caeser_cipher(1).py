def encryption(text, key):
    cipher = ""
    for i in text:
        if i != " ":
            cipher += chr(((ord(i)-ord('a')+key) % 26)+ord('a'))
        else:
            cipher += " "
    return cipher


def decryption(cipher, key):
    text = ""
    for i in cipher:
        if i != " ":
            text += chr(((ord(i)-ord('a')-key) % 26)+ord('a'))
        else:
            text += " "
    return text


key = int(input("Enter Key: "))
cipher = encryption(input("Enter Plain text: "), key)
text = decryption(cipher, key)
print(f'Cipher text: {cipher.upper()}', f'Plain text: {text}', sep="\n")
