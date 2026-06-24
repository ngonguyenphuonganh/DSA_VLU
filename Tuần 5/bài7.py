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
_, parent_b7 = dijkstra_multi_features(adj_G1, s=0, n=6) 

def get_shortest_path(parent, start, target):
    path = []
    curr = target
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]

path_0_to_4 = get_shortest_path(parent_b7, start=0, target=4)
print(f"Bài 7: Truy vết đường đi: {' -> '.join(map(str, path_0_to_4))}") 
