def stable_sort(a):
    # a là mảng các tuple (khóa, nhãn)
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(stable_sort([(2, 'a'), (1, 'b'), (2, 'c')]))