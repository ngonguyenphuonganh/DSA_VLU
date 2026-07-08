from collections import deque

def min_sliding_window(A, k):
    dq = deque()
    res = []
    
    for i in range(len(A)):
        # Bỏ các phần tử nằm ngoài cửa sổ hiện tại khỏi đầu Deque
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # Duy trì tính đơn điệu TĂNG DẦN: bỏ các phần tử lớn hơn A[i] ở đuôi Deque
        while dq and A[dq[-1]] > A[i]:
            dq.pop()
            
        dq.append(i)
        
        # Khi cửa sổ đủ kích thước, lưu kết quả
        if i >= k - 1:
            res.append(A[dq[0]])
            
    return res

A = [4, 2, 12, 11, -5, 8, 1, 5, 6]
k = 3
print("Min trong cửa sổ trượt (Câu 5):", min_sliding_window(A, k))
# Output: [2, 2, -5, -5, -5, 1, 1]