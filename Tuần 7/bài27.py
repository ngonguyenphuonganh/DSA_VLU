import random

SECRET = random.randint(1, 10**9)

def secure_hash(key, m):
    return hash((key, SECRET)) % m