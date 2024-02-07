import random


def rabin(n):
    if n <= 1 :
        return False
    if n == 2 or n == 3 :
        return True
    if n%2 == 0 :
        return False
    k, q = 0, n-1
    while q%2 == 0:
        k += 1
        q //= 2
    a = random.randint(2, n-2)
    x = pow(a, q, n)
    if x == 1 or x == n-1:
        return True
    for i in range(0, k-1):
        x = pow(x, 2, n)
        if x == n-1:
            return True
    return False

p = int(input())
print(rabin(p))