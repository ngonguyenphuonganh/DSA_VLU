INF = float('inf')
cities = ['A', 'B', 'C', 'D', 'E']
n_G2 = 5

adj_G2 = [[] for _ in range(n_G2)]

edges = [
    (0, 1, 5),  
    (0, 2, 3),  
    (1, 2, 1),  
    (1, 3, 2),  
    (2, 3, 6),  
    (3, 4, 4)   
]

for u, v, w in edges:
    adj_G2[u].append((v, w))
    adj_G2[v].append((u, w))

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
        if u == -1: break
        visited[u] = True
        
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist

dist_from_A = dijkstra(adj_G2, s=0, n=n_G2)

print("=== KẾT QUẢ BÀI 5 ===")
print("Khoảng cách ngắn nhất từ thành phố A:")
for i in range(n_G2):
    print(f"Từ A -> {cities[i]}: {dist_from_A[i]}")
