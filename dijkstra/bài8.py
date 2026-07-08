INF = float('inf')
adj_G1 = [
    [(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)],
    [(4, 3), (5, 6)], [(5, 2)], []
]

def dijkstra_multi_features(adj, s, n, target=-1):
    dist = [INF] * n
    parent = [-1] * n  
    visited = [False] * n
    dist[s] = 0
    
    for _ in range(n):
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
                
        if u == -1: break
        if u == target:
            break
            
        visited[u] = True
        
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u  
                
    return dist, parent
dist_b8, _ = dijkstra_multi_features(adj_G1, s=0, n=6)
D = 3
valid_nodes = [node for node, d in enumerate(dist_b8) if d <= D]
print(f"Bài 8: Số đỉnh trong bán kính D={D} là: {len(valid_nodes)} đỉnh {valid_nodes}") 