import time
def benchmark_chaining(data, size):
    table = [[] for _ in range(size)]
    t0 = time.time()
    for x in data:
        table[x % size].append(x)
    return time.time() - t0

def benchmark_probing(data, size):
    table = [None] * size
    t0 = time.time()
    for x in data:
        idx = x % size
        while table[idx] is not None:
            idx = (idx + 1) % size
        table[idx] = x
    return time.time() - t0