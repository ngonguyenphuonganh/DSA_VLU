deque_list = []
def pushFront(val):
    deque_list.insert(0, val)
def pushBack(val):
    deque_list.append(val)
def popFront():
    return deque_list.pop(0) if deque_list else None
def popBack():
    return deque_list.pop() if deque_list else None