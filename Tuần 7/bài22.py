def tuple_hash(pair):
    a, b = pair
    h1 = hash(a)
    h2 = hash(b)
    return h1 ^ (h2 + 0x9e3779b9 + (h1 << 6) + (h1 >> 2))