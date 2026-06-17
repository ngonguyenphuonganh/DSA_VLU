def unstable_example():
    a = [(2, 'a'), (2, 'b'), (1, 'c')]
    for i in range(len(a)):
        min_i = i
        for j in range(i + 1, len(a)):
            if a[j][0] < a[min_i][0]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a 