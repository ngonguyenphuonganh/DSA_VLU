class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def bai_14(head):
    temp = head
    while temp:
        min_node = temp
        r = temp.next
        while r:
            if r.data < min_node.data:
                min_node = r
            r = r.next
        temp.data, min_node.data = min_node.data, temp.data
        temp = temp.next
    return head