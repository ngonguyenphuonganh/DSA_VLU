def tim_so_chan_dau_tien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1
a = list(map(int, input("Nhập mảng: ").split()))
ket_qua = tim_so_chan_dau_tien(a)
print("Vị trí số chẵn đầu tiên:", ket_qua)