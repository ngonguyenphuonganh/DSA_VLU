import random

def selection_counts(a):
    a = a[:]
    n = len(a)
    comps = 0
    swaps = 0
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_i]:
                min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
            swaps += 1
    return comps, swaps

def demo_best_avg_worst(n=10, seed=0):
    random.seed(seed)
    best = list(range(n))
    worst = list(range(n, 0, -1))
    avg = best[:]
    random.shuffle(avg)

    return {
        "best": selection_counts(best),
        "avg": selection_counts(avg),
        "worst": selection_counts(worst),
        "expected_comps": n * (n - 1) // 2
    }