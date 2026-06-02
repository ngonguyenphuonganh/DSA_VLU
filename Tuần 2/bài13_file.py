import math
def single_element(array):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if mid % 2 == 1:
            mid = mid - 1
            
        if mid + 1 < len(array) and array[mid] == array[mid + 1]:
            start = mid + 2
        else:
            end = mid - 1
    return array[start]

array = list(map(int, input("Nhập mảng số: ").split()))
print("Phần tử đơn lẻ là:", single_element(array))