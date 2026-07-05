def delete_by_value(head, x):
    if not head:
        return None
    if head.val == x:
        return head.next
    curr = head
    while curr.next and curr.next.val != x:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return head