def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
n = int(input("Nhap so phan tu: "))
arr = []
for i in range(n):
    key = int(input("Nhap key: "))
    value = input("Nhap value: ")
    arr.append([key, value])
bubble_sort(arr)
print(arr)