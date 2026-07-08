def tim_max(a):
    max_value = a[0]
    vi_tri = 0
    for i in range(len(a)):
        if a[i] > max_value:
            max_value = a[i]
            vi_tri = i
    return max_value, vi_tri
a = list(map(int, input("Nhập mảng: ").split()))
gia_tri, vi_tri = tim_max(a)
print("Giá trị lớn nhất:", gia_tri)
print("Vị trí:", vi_tri)