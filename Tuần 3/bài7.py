def bubble_sort_char(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = input("Nhap cac ky tu: ").split()
bubble_sort_char(arr)
print(arr)