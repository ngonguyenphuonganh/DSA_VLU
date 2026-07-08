class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle_start(head):
    slow = fast = head
    has_cycle = False
    
    # Giai đoạn 1: Rùa chạy 1, Thỏ chạy 2 tìm điểm gặp nhau
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
            
    if not has_cycle:
        return None
        
    # Giai đoạn 2: Trả 1 con trỏ về Head, đi cùng tốc độ 1 bước
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
        
    return slow # Chính là đỉnh bắt đầu chu trình