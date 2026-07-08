INF = float('inf')
dist_G1 = [0, 3, 1, 4, 7, 9]

def print_distances(dist):
    print("=== KẾT QUẢ BÀI 4 ===")
    for i in range(len(dist)):
        if dist[i] == INF:
            print(f"Khoảng cách từ 0 -> {i}: -1")
        else:
            print(f"Khoảng cách từ 0 -> {i}: {dist[i]}")
print_distances(dist_G1)