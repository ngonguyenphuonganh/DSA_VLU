def dem_so_sanh(A, x):
    count = 0
    for i in range(len(A)):
        count += 1
        if A[i] == x:
            return count
    return count
A = [7, 3, 9, 12, 5, 8, 1]
print("x = 7:", dem_so_sanh(A, 7))
print("x = 1:", dem_so_sanh(A, 1))
print("x = 100:", dem_so_sanh(A, 100))

#x=7 => 1 phép so sánh
#x=1=> 7 phép so sánh
#x=100(không tồn tại) nên phải duyệt=> 7 phép so sánh

