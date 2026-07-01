capacity = 3
stack = []

def push(val):
    if len(stack) >= capacity:
        print("Overflow")
    else:
        stack.append(val)

def pop():
    if not stack:
        print("Underflow")
        return None
    return stack.pop()