def insert_sorted(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i - 1] > a[i]:
        a[i], a[i - 1] = a[i - 1], a[i]
        i -= 1
    return a

print(insert_sorted([1, 3, 5, 7], 4)) # Output: [1, 3, 4, 5, 7]