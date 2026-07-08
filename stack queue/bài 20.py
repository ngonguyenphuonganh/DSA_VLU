in_stack = []
out_stack = []

def enqueue_using_stacks(val):
    in_stack.append(val)

def dequeue_using_stacks():
    if not out_stack:
        while in_stack:
            out_stack.append(in_stack.pop())
    return out_stack.pop() if out_stack else None