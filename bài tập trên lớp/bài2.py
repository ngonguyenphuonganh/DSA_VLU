def count_shifts(a):
    shifts = 0
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return shifts

A = [5, 2, 4, 6, 1, 3]
print("Tổng số lần dịch chuyển (Câu 2):", count_shifts(A)) 
# Output: 9