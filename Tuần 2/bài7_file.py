import math
def upper_bound(array, element):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    kq = len(array)
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if array[mid] > element:
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
print("Upper bound là:", upper_bound(array, element))