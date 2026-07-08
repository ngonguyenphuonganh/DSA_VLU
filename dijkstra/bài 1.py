adj = [[] for _ in range(6)]

adj[0] = [(1, 4), (2, 1)]
adj[1] = [(3, 1)]
adj[2] = [(1, 2), (3, 5), (4, 8)]
adj[3] = [(4, 3), (5, 6)]
adj[4] = [(5, 2)]
adj[5] = []

print("Danh sách kề của đồ thị G1:")
for u in range(6):
    print(f"adj[{u}] = {adj[u]}")