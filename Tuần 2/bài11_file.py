import math
def find_min_rotated(array):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    kq = array[0]
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if array[start] <= array[end]:
            if array[start] < kq:
                kq = array[start]
            break
        if array[mid] < kq:
            kq = array[mid]
            
        if array[start] <= array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return kq

array = list(map(int, input("Nhập mảng số: ").split()))
print("Phần tử nhỏ nhất là:", find_min_rotated(array))