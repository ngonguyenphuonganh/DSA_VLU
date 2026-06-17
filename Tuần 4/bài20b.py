import heapq
def heap_sort_ascending(a):
    h = a[:]
    heapq.heapify(h)
    res = []
    while h:
        res.append(heapq.heappop(h))
    return res