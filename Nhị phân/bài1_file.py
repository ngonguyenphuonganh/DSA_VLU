def binary_search(array, element):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == element:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
kq = binary_search(array, element)
print("Phan tu tim kiem duoc la:", kq)