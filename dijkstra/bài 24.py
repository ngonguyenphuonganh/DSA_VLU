import heapq
INF = 10**18
def prove_astar_vs_dijkstra():
    R, C = 5, 5
    start, target = (0, 0), (4, 4)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def run_dijkstra():
        dist = {(r, c): INF for r in range(R) for c in range(C)}
        dist[start] = 0

        pq = [(0, start[0], start[1])]
        nodes_popped = 0

        while pq:
            d, r, c = heapq.heappop(pq)
            nodes_popped += 1

            if (r, c) == target:
                return nodes_popped

            if d > dist[(r, c)]:
                continue

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    new_d = d + 1

                    if new_d < dist[(nr, nc)]:
                        dist[(nr, nc)] = new_d
                        heapq.heappush(pq, (new_d, nr, nc))

        return nodes_popped
    def run_astar():
        def h(r, c):
            return abs(r - target[0]) + abs(c - target[1])

        g_score = {(r, c): INF for r in range(R) for c in range(C)}
        g_score[start] = 0
        pq = [(h(0, 0), 0, 0, start[0], start[1])]
        nodes_popped = 0

        while pq:
            f, neg_g, g, r, c = heapq.heappop(pq)
            nodes_popped += 1

            if (r, c) == target:
                return nodes_popped

            if g > g_score[(r, c)]:
                continue

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < R and 0 <= nc < C:
                    new_g = g + 1

                    if new_g < g_score[(nr, nc)]:
                        g_score[(nr, nc)] = new_g
                        f_score = new_g + h(nr, nc)

                        heapq.heappush(pq, (f_score, -new_g, new_g, nr, nc))

        return nodes_popped

    print("Bài 24 - Số đỉnh Dijkstra phải duyệt:", run_dijkstra())
    print("Bài 24 - Số đỉnh A* phải duyệt:      ", run_astar())