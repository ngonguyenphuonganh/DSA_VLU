stack = []
min_stack = []

def push_min(val):
    stack.append(val)
    if not min_stack or val <= min_stack[-1]:
        min_stack.append(val)

def pop_min():
    if stack:
        val = stack.pop()
        if val == min_stack[-1]:
            min_stack.pop()
        return val

def getMin():
    return min_stack[-1] if min_stack else None