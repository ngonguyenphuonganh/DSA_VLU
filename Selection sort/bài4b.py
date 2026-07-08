def bai_4(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if i < len(arr) - 1: # In trạng thái sau mỗi vòng (trừ vòng cuối cùng thừa)
            print(f"Sau vòng {i + 1}: {arr}")