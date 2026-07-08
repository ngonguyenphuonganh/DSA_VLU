import heapq

INF = 10**18

def second_shortest_path(adj, s, t, n):
    dist1 = [INF] * n  # Ngắn nhất
    dist2 = [INF] * n  # Ngắn nhì

    dist1[s] = 0

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        # Nếu d còn lớn hơn cả Top 2 ghi nhận được -> vô giá trị
        if d > dist2[u]:
            continue

        for v, w in adj[u]:
            new_d = d + w

            if new_d < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_d
                heapq.heappush(pq, (new_d, v))

            elif dist1[v] < new_d < dist2[v]:
                dist2[v] = new_d
                heapq.heappush(pq, (new_d, v))

    return dist1[t], dist2[t]
adj_G1 = {
0: [(1, 1), (2, 4)],
1: [(2, 2), (3, 5)],
2: [(3, 1)],
3: []
}
shortest, second = second_shortest_path(adj_G1, s=0, t=3, n=4)
print("Đường đi ngắn nhất:", shortest)
print("Đường đi ngắn nhì:", second)