import math

def multi_hash(k, m):
    A = (math.sqrt(5) - 1) / 2
    return math.floor(m * ((k * A) % 1))