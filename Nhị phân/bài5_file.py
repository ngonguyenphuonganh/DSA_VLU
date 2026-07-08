import math
def count_occurrences(array, element):
#vitridau 
    start, end = 0, len(array) - 1
    first = -1
    step = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if element == array[mid]:
            first = mid
            end = mid - 1
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if first == -1:
        return 0

#vitricuoi
    start, end = 0, len(array) - 1
    last = -1
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if element == array[mid]:
            last = mid
            start = mid + 1
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return last - first + 1

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
kq = count_occurrences(array, element)
print("Số lần xuất hiện là:", kq)