import math
def integer_sqrt(n):
    mid = 0
    start = 0
    end = n
    step = 0
    kq = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if mid * mid == n:
            return mid
        if mid * mid < n:
            kq = mid
            start = mid + 1
        else:
            end = mid - 1
    return kq

n = int(input("Nhập số nguyên n: "))
kq = integer_sqrt(n)
print("Phần nguyên căn bậc hai là:", kq)