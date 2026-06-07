def dem_nghich_the(arr):
    n = len(arr)
    dem = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                dem += 1
    return dem

def bubble_sort_dem_swap(arr):
    n = len(arr)
    dem_swap = 0
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dem_swap += 1
    return dem_swap
arr = list(map(int, input("Nhap mang so: ").split()))
arr2 = arr.copy()
print("So nghich the:", dem_nghich_the(arr))
print("So swap:", bubble_sort_dem_swap(arr2))