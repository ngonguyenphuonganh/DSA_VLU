def modulo_hashing(keys, m):
    table = [[] for _ in range(m)]
    for k in keys:
        table[k % m].append(k)
    return table