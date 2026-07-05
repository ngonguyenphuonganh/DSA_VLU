def create_hashset(size=10):
    return [[] for _ in range(size)]

def add_set(hset, key):
    idx = hash(key) % len(hset)
    if key not in hset[idx]:
        hset[idx].append(key)

def contains_set(hset, key):
    idx = hash(key) % len(hset)
    return key in hset[idx]

def remove_set(hset, key):
    idx = hash(key) % len(hset)
    if key in hset[idx]:
        hset[idx].remove(key)