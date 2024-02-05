def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_input():
    while True:
        try:
            num = int(input("Enter a prime number: "))
            if is_prime(num):
                return num
            else:
                print("Please enter a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    print(phi)
    e = 2
    while gcd(e, phi) != 1:
        e += 1
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))


def encrypt(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text


def main():
    print("RSA Encryption and Decryption without random module")

    p = get_prime_input()
    q = get_prime_input()

    public_key, private_key = generate_keypair(p, q)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = input("Enter a message to encrypt: ")

    cipher_text = encrypt(message, public_key)
    print("Encrypted Message:", cipher_text)
    cipher = [i % 127 for i in cipher_text]
    cipher_ = [chr(i) for i in cipher_text]
    print("Encrypted Message:", ''.join(cipher_))
    decrypted_message = decrypt(cipher_text, private_key)
    print("Decrypted Message:", decrypted_message)


main()
