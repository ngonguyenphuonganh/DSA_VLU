stack = [1, 2, 3]
temp_stack = []
count = 0

while stack:
    val = stack.pop()
    print(val, end=" ")
    temp_stack.append(val)
    count += 1
print(f"\n{count}")

while temp_stack:
    stack.append(temp_stack.pop())