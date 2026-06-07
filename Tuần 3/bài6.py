def one_pass(arr):
    n = len(arr)
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Nhap mang so: ").split()))
one_pass(arr)
print("Mang sau 1 luot:", arr)
print("Phan tu cuoi:", arr[-1])