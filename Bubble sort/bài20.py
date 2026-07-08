def merge_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, dem_left = merge_count(arr[:mid])
    right, dem_right = merge_count(arr[mid:])
    i = 0
    j = 0
    merged = []
    dem = dem_left + dem_right
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            dem += len(left) - i
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged, dem
arr = list(map(int, input("Nhap mang so: ").split()))
mang_sap_xep, so_swap = merge_count(arr)
print("So swap:", so_swap)
