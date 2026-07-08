def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    base, prime = 256, 101
    h = pow(base, m - 1) % prime
    p_hash, t_hash = 0, 0
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        t_hash = (base * t_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i + m] == pattern:
            return i
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            t_hash = (t_hash + prime) % prime
    return -1