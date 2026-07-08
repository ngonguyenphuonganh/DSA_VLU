def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def tim_so_nguyen_to_dau_tien(a):
    for i in range(len(a)):
        if kiem_tra_so_nguyen_to(a[i]):
            return a[i], i
    return -1, -1
a = list(map(int, input("Nhập mảng: ").split()))
so, vi_tri = tim_so_nguyen_to_dau_tien(a)
print("Số nguyên tố đầu tiên:", so)
print("Vị trí:", vi_tri)