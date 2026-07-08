def chi_square(buckets, total_keys):
    m = len(buckets)
    expected = total_keys / m
    return sum((x - expected) ** 2 / expected for x in buckets)