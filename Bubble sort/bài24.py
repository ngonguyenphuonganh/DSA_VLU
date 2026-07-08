def mot_luot_bubble_sort(arr, i):
    n = len(arr)

    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

start = list(map(int, input("Nhap mang ban dau: ").split()))
target = list(map(int, input("Nhap mang sau: ").split()))

arr = start.copy()

if arr == target:
    print("So luot it nhat:", 0)
else:
    tim_thay = False

    for i in range(len(arr)):
        mot_luot_bubble_sort(arr, i)

        if arr == target:
            print("So luot it nhat:", i + 1)
            tim_thay = True
            break

    if tim_thay == False:
        print("Khong the tao ra mang sau bang bubble sort")