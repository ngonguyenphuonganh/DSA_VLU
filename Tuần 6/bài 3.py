operations = ["push 5", "push 7", "pop"]
stack = []
for op in operations:
    if op.startswith("push"):
        val = int(op.split()[1])
        stack.append(val)
    elif op == "pop" and stack:
        print(stack.pop())
print(stack)