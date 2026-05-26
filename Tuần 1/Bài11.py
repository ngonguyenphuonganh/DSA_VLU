def vi_tri_cuoi(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1
a = list(map(int, input("Nhập mảng: ").split()))
x = int(input("Nhập số cần tìm: "))
ket_qua = vi_tri_cuoi(a, x)
print("Vị trí cuối:", ket_qua)