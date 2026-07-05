def quadratic_insert(table, key):
    size = len(table)
    h = hash(key) % size
    i = 0
    while i < size:
        idx = (h + i * i) % size
        if table[idx] is None:
            table[idx] = key
            return True
        i += 1
    return False

def double_hash_insert(table, key):
    size = len(table)
    h1 = hash(key) % size
    h2 = 7 - (hash(key) % 7)
    i = 0
    while i < size:
        idx = (h1 + i * h2) % size
        if table[idx] is None:
            table[idx] = key
            return True
        i += 1
    return False