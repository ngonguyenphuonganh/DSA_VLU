def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
        if j >= 0:
            comparisons += 1
        arr[j + 1] = key
    return comparisons, shifts