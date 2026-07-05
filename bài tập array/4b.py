def insert_after_node(prev_node, new_val):
    if not prev_node:
        return
    new_node = (new_val)
    new_node.next = prev_node.next
    prev_node.next = new_node

def insert_after_index(head, k, new_val):
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next
    if curr:
        insert_after_node(curr, new_val)
    return head