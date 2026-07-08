queue = [1, 2, 3]
stack = []
while queue:
    stack.append(queue.pop(0))
while stack:
    queue.append(stack.pop())