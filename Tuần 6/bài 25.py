pq = []
def insert_pq(val):
    pq.append(val)
    pq.sort(reverse=True)

def extract_max():
    return pq.pop(0) if pq else None