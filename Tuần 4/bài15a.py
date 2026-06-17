class ListNode:
    def __init__(self, val=0):
        self.val=val
        self.next= None
def is_15(head):
    dummy = ListNode(0)
    curr = head
    while curr:
        nxt = curr.next
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        curr.next = prev.next
        prev.next = curr
        curr = nxt
        return dummy.next