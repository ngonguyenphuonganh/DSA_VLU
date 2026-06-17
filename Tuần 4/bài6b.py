def bai_6(arr):
    comp_count = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comp_count += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    print("Số lần so sánh:", comp_count)
    return arr