capacity = 3
queue = []

def enqueue_check(val):
    if len(queue) == capacity:
        print("Lỗi")
    else:
        queue.append(val)

def dequeue_check():
    if not queue:
        print("Lỗi")
        return None
    return queue.pop(0)

def count():
    return len(queue)