import heapq

def max_probability_path(adj_prob, s, t, n):
    # mảng lưu xác suất cao nhất, khởi tạo toàn 0.0
    prob = [0.0] * n
    prob[s] = 1.0  # 100% sống sót ở vạch xuất phát

    # Python chỉ có min-heap, gán dấu trừ để giả lập Max-Heap
    pq = [(-1.0, s)]

    while pq:
        p_u, u = heapq.heappop(pq)
        p_u = -p_u  # Trả lại giá trị dương

        if u == t:
            return p_u

        if p_u < prob[u]:
            continue

        for v, edge_prob in adj_prob[u]:
            new_prob = p_u * edge_prob

            if new_prob > prob[v]:  # Tìm thấy xác suất sống cao hơn
                prob[v] = new_prob
                heapq.heappush(pq, (-new_prob, v))

    return 0.0