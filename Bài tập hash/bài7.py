def create_rehash_table(capacity=4):
    return {"buckets": [[] for _ in range(capacity)], "size": 0, "capacity": capacity}

def put_rehash(ht, key, value):
    if ht["size"] / ht["capacity"] >= 0.75:
        old_buckets = ht["buckets"]
        ht["capacity"] *= 2
        ht["buckets"] = [[] for _ in range(ht["capacity"])]
        ht["size"] = 0
        for bucket in old_buckets:
            for k, v in bucket:
                put_rehash(ht, k, v)
    idx = hash(key) % ht["capacity"]
    for pair in ht["buckets"][idx]:
        if pair[0] == key:
            pair[1] = value
            return
    ht["buckets"][idx].append([key, value])
    ht["size"] += 1