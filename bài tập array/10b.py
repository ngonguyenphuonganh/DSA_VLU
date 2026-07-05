def remove_nth_from_end(head, k):
    dummy = (0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(k + 1):
        if fast:
            fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    if slow and slow.next:
        slow.next = slow.next.next
    return dummy.next