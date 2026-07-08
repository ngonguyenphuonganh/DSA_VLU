def simulate_amortized_append(n):
    capacity = 1
    size = 0
    total_copies = 0
    for _ in range(n):
        if size == capacity:
            total_copies += size
            capacity *= 2
        size += 1
        total_copies += 1
    return total_copies / n