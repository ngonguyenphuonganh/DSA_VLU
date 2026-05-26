def tim_tat_ca(a, x):
    ds = []
    for i in range(len(a)):
        if a[i] == x:
            ds.append(i)
    return ds
a = list(map(int, input("Nhập mảng: ").split()))
x = int(input("Nhập số cần tìm: "))
ket_qua = tim_tat_ca(a, x)
print("Các vị trí:", ket_qua)