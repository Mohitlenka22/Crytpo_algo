import random


def miller_ra(n):
    t = n-1
    k = 0
    while t % 2 != 0:
        k = k+1
        t //= 2

    a = random.randrange(1, n-1)
    if (pow(a, t, n) == 1):
        return 1
    for j in range(k-1):
        if (pow(a, pow(2, j)*t, n) == n-1):
            return 1
    return 0


# for x in range(100):
#     print(x, miller_ra(x))

print(miller_ra(19))
