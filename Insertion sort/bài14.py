def sort_multi_keys(a):
    for i in range(1, len(a)):
        key = a[i] # (Tên, Điểm)
        j = i - 1
        # Điểm giảm dần, nếu bằng thì Tên tăng dần
        while j >= 0 and (a[j][1] < key[1] or (a[j][1] == key[1] and a[j][0] > key[0])):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(sort_multi_keys([('An', 8), ('Ba', 9), ('Cu', 8)]))