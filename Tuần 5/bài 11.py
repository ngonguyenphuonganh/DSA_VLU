import heapq
INF = float('inf')

adj_G1 = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]

def dijkstra_multisource(adj, sources, n):
    dist = [INF] * n
    pq = []
    
    for s in sources:
        dist[s] = 0
        heapq.heappush(pq, (0, s))
        
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

print("Bài 11 (Nhiều nguồn {0, 3}):", dijkstra_multisource(adj_G1, sources=[0, 3], n=6))
