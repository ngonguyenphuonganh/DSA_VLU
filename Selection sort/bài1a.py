def is_1(a, x):
    a.append(x)
    n = len(a)
    j = n - 2
    while j >= 0 and a[j] > x:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = x
    return a