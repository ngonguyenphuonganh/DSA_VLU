def detect_cycle_start(head):
    slow = fast = head
    has_cyc = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cyc = True
            break
    if not has_cyc:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow