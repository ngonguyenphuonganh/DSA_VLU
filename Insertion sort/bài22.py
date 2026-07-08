def count_shifts(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return shifts
def bubble_swaps(a):
    arr = a.copy()
    swaps = 0
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

def selection_swaps(a):
    arr = a.copy()
    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps += 1
    return swaps

test_arr = [64, 34, 25, 12, 22, 11, 90]
print("Insertion:", count_shifts(test_arr.copy()))
print("Bubble:", bubble_swaps(test_arr))
print("Selection:", selection_swaps(test_arr))
