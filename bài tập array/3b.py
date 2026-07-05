def search_index(head, target):
    index = 0
    curr = head
    while curr:
        if curr.val == target:
            return index
        curr = curr.next
        index += 1
    return -1