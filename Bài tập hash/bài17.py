def string_hash(s, m):
    total = 0
    for char in s:
        total += ord(char)
    return total % m