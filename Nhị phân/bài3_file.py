def first_occurrence(array, element):
    start = 0
    end = len(array) - 1
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == element:
            ans = mid      
            end = mid - 1  
        elif element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return ans

array = list(map(int, input("Nhập mảng số: ").split()))
element = int(input("Nhập số: "))
print(first_occurrence(array, element))