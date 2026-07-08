import heapq
graph = {
    0: [(1, 3), (2, 4)],
    1: [],
    2: [(1, -2)]
}
edges = [(0, 1, 3), (0, 2, 4), (2, 1, -2)]
n_vertices = 3

def dijkstra(start, target):
    dist = {i: float('inf') for i in range(n_vertices)}
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue 
        
        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    return dist[target]

def bellman_ford(start, target):
    dist = {i: float('inf') for i in range(n_vertices)}
    dist[start] = 0
    
    for _ in range(n_vertices - 1):
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
    return dist[target]

print("Đường đi A -> B bằng Dijkstra:", dijkstra(0, 1))     
print("Đường đi A -> B bằng Bellman-Ford:", bellman_ford(0, 1)) 