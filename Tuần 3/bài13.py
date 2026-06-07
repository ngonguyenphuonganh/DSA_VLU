import ast
def bubble_sort_pair(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = ast.literal_eval(input("Nhap mang cap: "))
bubble_sort_pair(arr)
print(arr)