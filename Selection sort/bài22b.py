def stable_inplace_selection_sort(a, key=lambda x: x):
    n = len(a)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if key(a[j]) < key(a[min_i]):
                min_i = j

        x = a[min_i]
        while min_i > i:
            a[min_i] = a[min_i - 1]
            min_i -= 1
        a[i] = x
    return a