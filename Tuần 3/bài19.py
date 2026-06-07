def da_sap_xep(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
def bubble_sort_dem_luot(arr):
    n = len(arr)
    so_luot = 0
    for i in range(n):
        swapped = False
        so_luot += 1
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if da_sap_xep(arr):
            break
        if swapped == False:
            break
    return so_luot
arr = list(map(int, input("Nhap mang so: ").split()))
print("So luot can thiet:", bubble_sort_dem_luot(arr))
print("Mang sau khi sap xep:", arr)