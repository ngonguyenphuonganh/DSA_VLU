def poly_hash(s, p=31, m=1000000009):
    h = 0
    p_pow = 1
    for char in s:
        h = (h + (ord(char) - 96) * p_pow) % m
        p_pow = (p_pow * p) % m
    return h