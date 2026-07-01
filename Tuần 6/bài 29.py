hit_queue = []

def hit(timestamp):
    hit_queue.append(timestamp)

def get_hits(timestamp):
    while hit_queue and timestamp - hit_queue[0] >= 300:
        hit_queue.pop(0)
    return len(hit_queue)