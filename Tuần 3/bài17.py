def bubble_sort_k_luot(arr, k):
    n = len(arr)
    for i in range(k):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Nhap mang so: ").split()))
k = int(input("Nhap k: "))
bubble_sort_k_luot(arr, k)
print(arr)
print("K phan tu lon nhat o cuoi:", arr[-k:])