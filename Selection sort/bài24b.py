import heapq
def k_smallest_partial_selection(a, k):
    a = a[:]              
    n = len(a)
    k = min(k, n)
    for i in range(k):
        min_i = i
        for j in range(i + 1, n):
            if a[j] < a[min_i]:
                min_i = j
        a[i], a[min_i] = a[min_i], a[i]
    return a[:k]
def k_smallest_heap(a, k):
    k = min(k, len(a))
    h = a[:]               
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(k)]