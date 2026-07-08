def min_hash_sig(s, num_hashes=50):
    sig = [float('inf')] * num_hashes
    for item in s:
        h = hash(item)
        for i in range(num_hashes):
            val = hash((h, i)) % 1000000007
            if val < sig[i]:
                sig[i] = val
    return sig

def jaccard_approx(sig1, sig2):
    matches = sum(1 for a, b in zip(sig1, sig2) if a == b)
    return matches / len(sig1)