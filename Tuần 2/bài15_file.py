import math
def find_closest(array, k, x):
    start = 0
    end = len(array) - k
    step = 0
    while (start < end):
        step = step + 1
        mid = (start + end) // 2
        if x - array[mid] > array[mid + k] - x:
            start = mid + 1
        else:
            end = mid
    kq = []
    for i in range(start, start + k):
        kq.append(array[i])
    return kq

array = list(map(int, input("Nhập mảng số: ").split()))
k = int(input("Nhập số lượng k: "))
x = int(input("Nhập số x: "))
print("K phần tử gần nhất:", find_closest(array, k, x))