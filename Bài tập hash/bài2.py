def create_linear_table(size=10):
    return [[None, None] for _ in range(size)]

def put_linear(table, key, value):
    size = len(table)
    idx = hash(key) % size
    while table[idx][0] is not None:
        if table[idx][0] == key:
            table[idx][1] = value
            return
        idx = (idx + 1) % size
    table[idx] = [key, value]

def get_linear(table, key):
    size = len(table)
    idx = hash(key) % size
    start = idx
    while table[idx][0] is not None:
        if table[idx][0] == key:
            return table[idx][1]
        idx = (idx + 1) % size
        if idx == start:
            break
    return None