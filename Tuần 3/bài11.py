def bubble_sort_abs(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Nhap mang so: ").split()))
bubble_sort_abs(arr)
print(arr)