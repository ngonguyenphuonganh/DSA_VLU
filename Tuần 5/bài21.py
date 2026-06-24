import heapq

INF = 10**18

def dijkstra_magic_ticket(adj, s, t, n):
    dist = [[INF] * 2 for _ in range(n)]
    dist[s][0] = 0

    pq = [(0, s, 0)]

    while pq:
        d, u, k = heapq.heappop(pq)

        if d > dist[u][k]:
            continue

        if u == t:
            return d

        for v, w in adj[u]:
            # Không dùng vé
            if d + w < dist[v][k]:
                dist[v][k] = d + w
                heapq.heappush(pq, (dist[v][k], v, k))

            # Dùng vé free nếu chưa dùng
            if k == 0:
                if d < dist[v][1]:
                    dist[v][1] = d
                    heapq.heappush(pq, (dist[v][1], v, 1))

    return min(dist[t][0], dist[t][1])