def bubble_sort_count_swap(arr):
    n = len(arr)
    dem = 0
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                dem += 1
    return dem
arr = list(map(int, input("Nhap mang so: ").split()))
so_lan_swap = bubble_sort_count_swap(arr)
print(arr)
print("So lan hoan doi:", so_lan_swap)