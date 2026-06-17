def bai_3(arr):
    for i in range(len(arr)):
        max_idx = i  # Tìm phần tử lớn nhất
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr