import heapq

INF = 10**18

def dijkstra_at_most_k_stops(adj, s, t, k_stops, n):
    max_edges = k_stops + 1

    # dist[u][e]: chi phí tới u bằng ĐÚNG e cạnh
    dist = [[INF] * (max_edges + 1) for _ in range(n)]

    dist[s][0] = 0
    pq = [(0, s, 0)]  # tuple: (cost, u, edges_used)

    while pq:
        d, u, e = heapq.heappop(pq)

        if d > dist[u][e]:
            continue

        if u == t:
            return d

        # Chỉ đi tiếp nếu số cạnh đã dùng chưa chạm giới hạn
        if e < max_edges:
            for v, w in adj[u]:
                new_cost = d + w

                if new_cost < dist[v][e + 1]:
                    dist[v][e + 1] = new_cost
                    heapq.heappush(pq, (new_cost, v, e + 1))

    return -1
adj_G1 = {
    0: [(1, 4), (2, 1)],
    1: [(3, 2), (4, 10)],
    2: [(3, 2), (4, 8)],
    3: [(4, 1), (5, 3)],
    4: [(5, 1)],
    5: []
}

print(
    "Bài 22 (0 -> 4 tối đa 2 cạnh):",
    dijkstra_at_most_k_stops(adj_G1, s=0, t=4, k_stops=1, n=6)
)