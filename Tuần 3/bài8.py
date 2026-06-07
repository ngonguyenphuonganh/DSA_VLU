def bubble_sort_k_pass(arr, k):
    n = len(arr)
    for i in range(min(k, n)):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
arr = list(map(int, input("Nhap mang so: ").split()))
k = int(input("Nhap k: "))
bubble_sort_k_pass(arr, k)
print("Mang sau", k, "luot:", arr)
print(is_sorted(arr))