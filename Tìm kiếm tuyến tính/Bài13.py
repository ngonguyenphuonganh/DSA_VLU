def min_max(a):
    min_value = a[0]
    max_value = a[0]
    vi_tri_min = 0
    vi_tri_max = 0
    for i in range(len(a)):
        if a[i] < min_value:
            min_value = a[i]
            vi_tri_min = i
        if a[i] > max_value:
            max_value = a[i]
            vi_tri_max = i
    return min_value, vi_tri_min, max_value, vi_tri_max
a = list(map(int, input("Nhập mảng: ").split()))
min_val, vt_min, max_val, vt_max = min_max(a)
print("Giá trị nhỏ nhất:", min_val)
print("Vị trí min:", vt_min)
print("Giá trị lớn nhất:", max_val)
print("Vị trí max:", vt_max)