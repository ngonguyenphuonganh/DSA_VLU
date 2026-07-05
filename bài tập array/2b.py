def get_length_and_print(head):
    length = 0
    curr = head
    while curr:
        print(curr.val, end=" ")
        length += 1
        curr = curr.next
    print()
    return length