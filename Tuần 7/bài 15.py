import bisect

def add_server(ring, server_map, server_name, replicas=3):
    for i in range(replicas):
        h = hash(f"{server_name}_{i}")
        bisect.insort(ring, h)
        server_map[h] = server_name

def get_server(ring, server_map, key):
    if not ring:
        return None
    h = hash(key)
    idx = bisect.bisect_right(ring, h)
    if idx == len(ring):
        idx = 0
    return server_map[ring[idx]]