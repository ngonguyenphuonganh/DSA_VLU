def selection_swap_count(a):
    a = a[:]  # copy
    n = len(a)
    swaps = 0
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        if min_i != i:
            a[i], a[min_i] = a[min_i], a[i]
            swaps += 1
    return swaps

def bubble_swap_count(a):
    a = a[:]
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps