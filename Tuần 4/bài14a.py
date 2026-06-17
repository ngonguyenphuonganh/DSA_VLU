def is_14(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and (key[1] > arr[j][1] or (key[1] == arr[j][1] and key[0] < arr[j][0])):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr