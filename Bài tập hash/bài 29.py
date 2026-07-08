def create_bloom(size=100):
    return [0] * size

def bloom_add(filter_arr, item):
    size = len(filter_arr)
    for i in range(3):
        idx = hash(f"{item}_{i}") % size
        filter_arr[idx] = 1

def bloom_check(filter_arr, item):
    size = len(filter_arr)
    return all(filter_arr[hash(f"{item}_{i}") % size] == 1 for i in range(3))