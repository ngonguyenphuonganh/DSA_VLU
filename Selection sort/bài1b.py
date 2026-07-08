def bai_1(arr):
    if len(arr) == 0: return arr
    min_idx = 0
    for j in range(1, len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[0], arr[min_idx] = arr[min_idx], arr[0]
    return arr