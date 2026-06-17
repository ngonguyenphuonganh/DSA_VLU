def bai_9(arr):
    n = len(arr)
    for i in range(n // 2):
        min_idx = i
        max_idx = i
        for j in range(i + 1, n - i):
            if arr[j] < arr[min_idx]:
                min_idx = j
            elif arr[j] > arr[max_idx]:
                max_idx = j
        # Đưa min về đầu
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        # Xử lý ngoại lệ nếu max_idx nằm đúng tại vị trí i vừa bị đổi chỗ
        if max_idx == i:
            max_idx = min_idx
        # Đưa max về cuối
        arr[n - i - 1], arr[max_idx] = arr[max_idx], arr[n - i - 1]
    return arr