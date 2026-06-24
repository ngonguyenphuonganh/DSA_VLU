import heapq

INF = 10**18

def precompute_all_pairs(adj, n):
    dist_matrix = []

    for source in range(n):
        dist = [INF] * n
        dist[source] = 0
        pq = [(0, source)]

        while pq:
            d, u = heapq.heappop(pq)

            if d > dist[u]:
                continue

            for v, w in adj[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))

        dist_matrix.append(dist)

    return dist_matrix
adj_G1 = {
0: [(1, 4), (2, 1)],
1: [(3, 2), (4, 10)],
2: [(3, 2), (4, 8)],
3: [(4, 1), (5, 3)],
4: [(5, 1)],
5: []
}
LOOKUP_TABLE = precompute_all_pairs(adj_G1, n=6)
print("Bài 23 (Tra nhanh k/c từ 0 -> 5):", LOOKUP_TABLE[0][5])
print("Bài 23 (Tra nhanh k/c từ 2 -> 4):", LOOKUP_TABLE[2][4])
