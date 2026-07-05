DELETED = "DELETED_LABEL"

def insert_lazy(table, key):
    size = len(table)
    idx = hash(key) % size
    while table[idx] is not None and table[idx] != DELETED:
        if table[idx] == key:
            return
        idx = (idx + 1) % size
    table[idx] = key

def remove_lazy(table, key):
    size = len(table)
    idx = hash(key) % size
    start = idx
    while table[idx] is not None:
        if table[idx] == key:
            table[idx] = DELETED
            return True
        idx = (idx + 1) % size
        if idx == start:
            break
    return False