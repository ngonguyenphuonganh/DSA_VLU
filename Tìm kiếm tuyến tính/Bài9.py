def dem_xuat_hien(a, x):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
    return count
a = list(map(int, input("Nhập mảng: ").split()))
x = int(input("Nhập số cần đếm: "))
ket_qua = dem_xuat_hien(a, x)
print("Số lần xuất hiện:", ket_qua)