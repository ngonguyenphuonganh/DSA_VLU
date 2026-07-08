import heapq
INF = float('inf')

def dijkstra_vertex_weights(adj, vertex_costs, s, n):
    dist = [INF] * n
    # Đứng ở điểm xuất phát s thì tốn ngay chi phí của đỉnh s
    dist[s] = vertex_costs[s] 
    pq = [(dist[s], s)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
            
        for v, edge_weight in adj[u]:
            # Tổng chi phí = Chi phí đến u + Trọng số cạnh (u->v) + Chi phí bước vào đỉnh v
            new_cost = dist[u] + edge_weight + vertex_costs[v]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    return dist