def check_exist(array, element):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == element:
            return True
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return False

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
print(check_exist(array, element))