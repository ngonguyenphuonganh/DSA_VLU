def is_18(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        pos = 0
        while pos < i and arr[pos] <= key:
            pos += 1
        for j in range(i, pos, -1):
            arr[j] = arr[j - 1]
        arr[pos] = key
    return arr