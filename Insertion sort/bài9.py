import bisect

def binary_insertion_sort(a):
    for i in range(1, len(a)):
        key = a[i]
        # Tìm vị trí chèn bằng nhị phân
        pos = bisect.bisect_right(a, key, 0, i)
        # Dịch chuyển mảng
        a = a[:pos] + [key] + a[pos:i] + a[i+1:]
    return a

print(binary_insertion_sort([5, 2, 4, 6, 1, 3]))