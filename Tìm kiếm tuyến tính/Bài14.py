def tim_ten(ds, ten):
    for i in range(len(ds)):
        if ds[i].lower() == ten.lower():
            return i
    return -1
ds = input("Nhập danh sách tên: ").split(",")
ten = input("Nhập tên cần tìm: ")
ket_qua = tim_ten(ds, ten)
print("Vị trí:", ket_qua)