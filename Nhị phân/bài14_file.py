import math
def search_matrix(matrix, element):
    rows = len(matrix)
    cols = len(matrix[0])
    mid = 0
    start = 0
    end = rows * cols - 1
    step = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        r = mid // cols
        c = mid % cols
        if element == matrix[r][c]:
            return True
        if element < matrix[r][c]:
            end = mid - 1
        else:
            start = mid + 1
    return False

rows = int(input("Nhập số hàng: "))
matrix = []
for i in range(rows):
    row = list(map(int, input(f"Nhập hàng {i+1}: ").split()))
    matrix.append(row)
element = int(input("Nhập số cần tìm: "))
kq = search_matrix(matrix, element)
print("Kết quả:", kq)