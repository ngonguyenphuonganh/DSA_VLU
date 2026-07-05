import random

def universal_hash(k, m, p=1000000007):
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    return ((a * k + b) % p) % m