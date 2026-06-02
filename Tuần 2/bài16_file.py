import math
def check_koko(piles, speed, h):
    hours = 0
    for p in piles:
        hours = hours + (p + speed - 1) // speed
    return hours <= h
def min_eating_speed(piles, h):
    start = 1
    max_p = piles[0]
    for p in piles:
        if p > max_p:
            max_p = p
    end = max_p
    step = 0
    kq = end
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_koko(piles, mid, h):
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

piles = list(map(int, input("Nhập các đống chuối: ").split()))
h = int(input("Nhập số giờ h: "))
print("Tốc độ ăn nhỏ nhất:", min_eating_speed(piles, h))