import math
def check_ship(weights, capacity, days):
    current_days = 1
    current_weight = 0
    for w in weights:
        if current_weight + w > capacity:
            current_days = current_days + 1
            current_weight = w
        else:
            current_weight = current_weight + w
    return current_days <= days

def ship_within_days(weights, days):
    max_w = weights[0]
    total_w = 0
    for w in weights:
        total_w = total_w + w
        if w > max_w:
            max_w = w
            
    start = max_w
    end = total_w
    step = 0
    kq = end
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_ship(weights, mid, days):
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

weights = list(map(int, input("Nhập mảng trọng lượng: ").split()))
days = int(input("Nhập số ngày D: "))
print("Sức chứa nhỏ nhất:", ship_within_days(weights, days))