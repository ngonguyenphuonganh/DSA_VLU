def bai_5(arr):
    swap_count = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i: # Chỉ đếm khi thực sự có hoán đổi
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1
    print("Số lần swap:", swap_count)
    return arr