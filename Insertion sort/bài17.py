def left_to_right_insertion(a):
    for i in range(1, len(a)):
        key = a[i]
        pos = 0
        while pos < i and a[pos] <= key:
            pos += 1
        a = a[:pos] + [key] + a[pos:i] + a[i+1:]
    return a