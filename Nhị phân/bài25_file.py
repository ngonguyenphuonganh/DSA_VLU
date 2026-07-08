import math
def check_magnets(position, force, m):
    count = 1
    last_pos = position[0]
    for i in range(1, len(position)):
        if position[i] - last_pos >= force:
            count = count + 1
            last_pos = position[i]
    return count >= m

def max_distance_magnets(position, m):
    position.sort()
    start = 1
    end = position[-1] - position[0]
    step = 0
    kq = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_magnets(position, mid, m):
            kq = mid
            start = mid + 1
        else:
            end = mid - 1
    return kq

position = list(map(int, input("Nhập vị trí các giỏ: ").split()))
m = int(input("Nhập số nam châm m: "))
print("Lực từ lớn nhất là:", max_distance_magnets(position, m))