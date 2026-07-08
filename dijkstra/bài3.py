INF = float('inf')
def dijkstra(adj, s, n):
    dist = [INF] * n
    dist[s] = 0
    visited = [False] * n
    for _ in range(n):
        u = -1
        min_dist = INF
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
                
        if u == -1:
            break
            
        visited[u] = True
        
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                
    return dist
adj = [
    [(1, 4), (2, 2)],  
    [(2, 5), (3, 10)], 
    [(4, 3)],        
    [(5, 11)],         
    [(3, 4)],          
    []                 
]
dist_from_0 = dijkstra(adj, s=0, n=6)
print(f"Khoảng cách ngắn nhất từ 0: {dist_from_0}")