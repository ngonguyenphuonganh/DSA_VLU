import math
def count_less_equal(matrix, target):
    count = 0
    n = len(matrix)
    row = n - 1
    col = 0
    while row >= 0 and col < n:
        if matrix[row][col] <= target:
            count = count + (row + 1)
            col = col + 1
        else:
            row = row - 1
    return count

def kth_smallest(matrix, k):
    n = len(matrix)
    start = matrix[0][0]
    end = matrix[n-1][n-1]
    step = 0
    kq = start
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if count_less_equal(matrix, mid) >= k:
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

n = int(input("Nhập kích thước n: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    matrix.append(row)
k = int(input("Nhập k: "))
print("Phần tử thứ k là:", kth_smallest(matrix, k))