myQueue = []
myQueue.append(1)
myQueue.append(2)
myQueue.append(3)
print(myQueue.pop(0))
front_element = myQueue[0] if myQueue else None
is_empty = len(myQueue) == 0