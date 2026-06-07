def bubble_sort_count_compare(arr):
    n = len(arr)
    dem = 0
    for i in range(n):
        for j in range(n - i - 1):
            dem += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return dem
arr = list(map(int, input("Nhap mang so: ").split()))
so_lan_so_sanh = bubble_sort_count_compare(arr)
print(arr)
print("So lan so sanh:", so_lan_so_sanh)