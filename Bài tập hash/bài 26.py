def multiset_hash(items):
    res = 0
    for item in items:
        h = hash(item)
        res ^= (h ^ (h >> 16)) * 0x85ebca6b
    return res