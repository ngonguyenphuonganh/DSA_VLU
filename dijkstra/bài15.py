import heapq

INF = 10**18

def dijkstra_on_grid(grid):
    R, C = len(grid), len(grid[0])
    dist = [[INF] * C for _ in range(R)]

    # Bước vào ô Start (0,0) tốn ngay chi phí của ô (0,0)
    dist[0][0] = grid[0][0]
    pq = [(grid[0][0], 0, 0)]  # tuple: (cost, r, c)

    # 4 hướng di chuyển: lên, xuống, trái, phải
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        d, r, c = heapq.heappop(pq)

        # Nếu đã chạm đích góc dưới bên phải
        if r == R - 1 and c == C - 1:
            return d

        if d > dist[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Kiểm tra ô kế bên có nằm trong bảng không
            if 0 <= nr < R and 0 <= nc < C:
                new_cost = d + grid[nr][nc]

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
    return -1
grid_3x3 = [
[1, 3, 1],
[1, 5, 1],
[4, 2, 1]
]