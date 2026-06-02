import math
def search_rotated(array, element):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if element == array[mid]:
            return mid
            
        if array[start] <= array[mid]:
            if array[start] <= element and element < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if array[mid] < element and element <= array[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
print("Vị trí tìm được là:", search_rotated(array, element))