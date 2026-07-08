import heapq

INF = 10**18

def dijkstra_bottleneck(adj, s, n):
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, weight in adj[u]:
            bottleneck = max(dist[u], weight)

            if bottleneck < dist[v]:
                dist[v] = bottleneck
                heapq.heappush(pq, (dist[v], v))

    return dist