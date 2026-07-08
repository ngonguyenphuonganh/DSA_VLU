def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
a = [1, 3, 5, 7, 9, 11]
print(binary_search(a, 7))

#Linear Search
#Không cần sắp xếp
#Duyệt từng phần tử
#O(n)

#Binary Search
#Bắt buộc mảng tăng dần
#Chia đôi dữ liệu
#O(log n)