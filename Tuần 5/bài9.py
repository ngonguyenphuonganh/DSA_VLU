import heapq
INF = float('inf')
adj_G1 = [
    [(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 6)], [(5, 2)], []
]

def dijkstra_minheap(adj, s, n):
    dist = [INF] * n
    dist[s] = 0
    pq = [(0, s)]
    
    while pq:
        d_u, u = heapq.heappop(pq)
        if d_u > dist[u]:
            continue
            
        for v, weight in adj[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
                
    return dist

print("Bài 9 (Min-Heap): Mảng dist[] =", dijkstra_minheap(adj_G1, s=0, n=6))