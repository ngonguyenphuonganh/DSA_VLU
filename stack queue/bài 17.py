k = 4
queue = [None] * k
head = tail = -1

def enqueue(val):
    global head, tail
    if (tail + 1) % k == head:
        return False
    if head == -1: head = 0
    tail = (tail + 1) % k
    queue[tail] = val
    return True

def dequeue():
    global head, tail
    if head == -1:
        return None
    val = queue[head]
    if head == tail:
        head = tail = -1
    else:
        head = (head + 1) % k
    return val