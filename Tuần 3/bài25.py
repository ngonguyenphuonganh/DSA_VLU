def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = list(map(int, input("Nhap mang so: ").split()))

bubble_sort(arr)

print(arr)

print("Bat bien vong lap:")
print("Sau luot thu i, i phan tu lon nhat da nam dung vi tri o cuoi mang.")

print("Chung minh:")
print("Moi luot bubble sort se dua phan tu lon nhat trong phan chua sap xep ve cuoi.")
print("Sau n - 1 luot, cac phan tu deu nam dung vi tri.")
print("Vay mang duoc sap xep tang dan.")