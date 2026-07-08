def selection_sort_with_steps(a):
    n = len(a)
    steps = []
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
        steps.append(a[:])
    return a, steps