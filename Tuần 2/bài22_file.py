import math
def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a
    x = len(a)
    y = len(b)
    start = 0
    end = x
    step = 0
    while (start <= end):
        step = step + 1
        partition_a = (start + end) // 2
        partition_b = (x + y + 1) // 2 - partition_a
        
        max_left_a = float('-inf') if partition_a == 0 else a[partition_a - 1]
        min_right_a = float('inf') if partition_a == x else a[partition_a]
        max_left_b = float('-inf') if partition_b == 0 else b[partition_b - 1]
        min_right_b = float('inf') if partition_b == y else b[partition_b]
        
        if max_left_a <= min_right_b and max_left_b <= min_right_a:
            if (x + y) % 2 == 1:
                return max(max_left_a, max_left_b) * 1.0
            else:
                return (max(max_left_a, max_left_b) + min(min_right_a, min_right_b)) / 2.0
        elif max_left_a > min_right_b:
            end = partition_a - 1
        else:
            start = partition_a + 1
    return 0.0

a = list(map(int, input("Nhập mảng a: ").split()))
b = list(map(int, input("Nhập mảng b: ").split()))
print("Trung vị là:", find_median(a, b))