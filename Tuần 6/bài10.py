q1 = []
q2 = []

def push_stack_using_q(val):
    q1.append(val)

def pop_stack_using_q():
    if not q1: return None
    while len(q1) > 1:
        q2.append(q1.pop(0))
    val = q1.pop(0)
    q1.extend(q2)
    q2.clear()
    return val