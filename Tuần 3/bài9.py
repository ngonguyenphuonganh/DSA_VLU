def bubble_sort_early_exit(arr):
    n = len(arr)
    so_luot = 0
    for i in range(n):
        swapped = False
        so_luot += 1
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return so_luot
arr = list(map(int, input("Nhap mang so: ").split()))
so_luot = bubble_sort_early_exit(arr)
print(arr)
print("So luot:", so_luot)