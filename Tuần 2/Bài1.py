import math
def binary_search(array, element):
   mid = 0
   start = 0
   end = len(array)
   step = 0
   while (start <= end):
    step = step+1
    mid = (start + end) // 2
    
    if element == array[mid]:
        return mid
    if element < array[mid]:
        end = mid - 1
    else:
        start = mid + 1
    return -1

array=list(map(int, input("Nhập mảng số:").split()))
element=int(input("Nhập số:"))
kq = binary_search(array, element)
print("Phan tu tim kiem duoc la:", kq)