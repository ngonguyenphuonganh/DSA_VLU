import math
def find_peak(array):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    n = len(array)
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        left_ok = (mid == 0 or array[mid] > array[mid - 1])
        right_ok = (mid == n - 1 or array[mid] > array[mid + 1])
        
        if left_ok and right_ok:
            return mid
        if mid < n - 1 and array[mid] < array[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

array = list(map(int, input("Nhập mảng số: ").split()))
print("Vị trí đỉnh là:", find_peak(array))