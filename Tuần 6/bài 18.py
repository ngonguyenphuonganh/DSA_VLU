operations = ["enq 5", "enq 7", "deq"]
queue = []
for op in operations:
    if op.startswith("enq"):
        val = int(op.split()[1])
        queue.append(val)
    elif op == "deq" and queue:
        print(queue.pop(0))
print(queue)