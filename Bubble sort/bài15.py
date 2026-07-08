def bubble_sort_name(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
def bubble_sort_score(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j][1] < arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
n = int(input("Nhap so hoc sinh: "))
arr = []
for i in range(n):
    ten, diem = input().split()
diem = int(diem)
arr.append([ten, diem])
bubble_sort_name(arr)
bubble_sort_score(arr)
print(arr)