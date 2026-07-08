def selection_sort_comparison_count(a):
    a = a[:]
    n = len(a)
    comps = 0

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            comps += 1
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return comps  