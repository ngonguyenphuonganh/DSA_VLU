import math

def check_stations(stations, max_dist, k):
    added = 0
    for i in range(len(stations) - 1):
        dist = stations[i+1] - stations[i]
        added = added + int(dist / max_dist)
    return added <= k

def min_max_distance(stations, k):
    start = 0.0
    end = stations[-1] - stations[0]
    step = 0
    # Do tìm trên số thực nên dùng lặp cố định 100 lần thay cho while (start <= end)
    for i in range(100):
        step = step + 1
        mid = (start + end) / 2
        if check_stations(stations, mid, k):
            end = mid
        else:
            start = mid
    return round(start, 6)

stations = list(map(int, input("Nhập vị trí trạm xăng: ").split()))
k = int(input("Nhập số trạm thêm k: "))
print("Khoảng cách tối ưu:", min_max_distance(stations, k))