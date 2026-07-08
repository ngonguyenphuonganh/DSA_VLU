myStack = []
myStack.append(1)
myStack.append(2)
myStack.append(3)
print(myStack.pop())
top_element = myStack[-1] if myStack else None
is_empty = len(myStack) == 0