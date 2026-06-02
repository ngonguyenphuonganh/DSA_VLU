import math
def find_kth_positive(array, k):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        missing = array[mid] - (mid + 1)
        if missing < k:
            start = mid + 1
        else:
            end = mid - 1
    return start + k

array = list(map(int, input("Nhập mảng số: ").split()))
k = int(input("Nhập số k: "))
print("Phần tử thứ k bị thiếu:", find_kth_positive(array, k))