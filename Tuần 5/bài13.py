import heapq

def count_shortest_paths(adj, s, n):
    dist = [float('inf')] * n
    ways = [0] * n

    dist[s] = 0
    ways[s] = 1

    pq = [(0, s)]

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in adj[u]:
            new_d = d + w

            if new_d < dist[v]:
                dist[v] = new_d
                ways[v] = ways[u]
                heapq.heappush(pq, (new_d, v))

            elif new_d == dist[v]:
                ways[v] += ways[u]

    return dist, ways