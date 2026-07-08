import heapq
INF = float('inf')
adj_G1 = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]

def k_shortest_paths(adj, s, t, K, n):
    count = [0] * n
    result_paths = []
    
    pq = [(0, s)]
    while pq and len(result_paths) < K:
        d, u = heapq.heappop(pq)
        count[u] += 1
        
        if u == t:
            result_paths.append(d)
        if count[u] <= K:
            for v, w in adj[u]:
                heapq.heappush(pq, (d + w, v))
                
    return result_paths

print("Bài 20 (3 đường đi từ 0 -> 4):", k_shortest_paths(adj_G1, s=0, t=4, K=3, n=6))
