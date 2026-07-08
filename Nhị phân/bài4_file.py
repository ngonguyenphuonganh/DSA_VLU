import math
def last_occurrence(array, element):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    kq = -1
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if element == array[mid]:
            kq = mid
            start = mid + 1
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return kq

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
print("Vị trí cuối cùng là:", last_occurrence(array, element))