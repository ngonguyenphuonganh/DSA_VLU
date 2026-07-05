class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def pushFront(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pushBack(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        curr = self.head
        res = []
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        res.append("null")
        print("-".join(res))