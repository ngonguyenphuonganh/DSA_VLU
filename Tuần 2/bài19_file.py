import math
def check_cows(positions, dist, count_cows):
    count = 1
    last_pos = positions[0]
    for i in range(1, len(positions)):
        if positions[i] - last_pos >= dist:
            count = count + 1
            last_pos = positions[i]
    return count >= count_cows
def aggressive_cows(positions, c):
    positions.sort()
    start = 1
    end = positions[-1] - positions[0]
    step = 0
    kq = 0
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_cows(positions, mid, c):
            kq = mid
            start = mid + 1
        else:
            end = mid - 1
    return kq

positions = list(map(int, input("Nhập vị trí chuồng: ").split()))
c = int(input("Nhập số bò c: "))
print("Khoảng cách lớn nhất là:", aggressive_cows(positions, c))