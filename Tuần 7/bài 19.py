def count_collisions(keys, m):
    buckets = [0] * m
    for k in keys:
        buckets[k % m] += 1
    collisions = 0
    for count in buckets:
        if count > 1:
            collisions += count - 1
    return collisions