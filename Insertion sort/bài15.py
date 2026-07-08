class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertion_sort_list(head):
    dummy = ListNode(0)
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        next_node = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = next_node
    return dummy.next