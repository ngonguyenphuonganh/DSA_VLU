def bubble_sort(arr):
    n = len(arr)
    so_luot = 0
    for i in range(n):
        swapped = False
        so_luot += 1
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return so_luot
def cocktail_sort(arr):
    start = 0
    end = len(arr) - 1
    so_vong = 0
    while start < end:
        swapped = False
        so_vong += 1
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        end -= 1
        for i in range(end, start, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapped = True
        start += 1
        if not swapped:
            break
    return so_vong
arr = list(map(int, input("Nhap mang so: ").split()))
arr1 = arr.copy()
arr2 = arr.copy()
luot_bubble = bubble_sort(arr1)
luot_cocktail = cocktail_sort(arr2)
print("Bubble Sort:", arr1, "- so luot:", luot_bubble)
print("Cocktail Sort:", arr2, "- so vong:", luot_cocktail)

