def daily_temperatures(T):
    n = len(T)
    res = [0] * n
    stack = [] # Ngăn xếp lưu chỉ số (index)
    
    for i in range(n):
        # Trong khi stack không rỗng và nhiệt độ hiện tại lớn hơn nhiệt độ của ngày ở đỉnh stack
        while stack and T[i] > T[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index # Số ngày chờ
        stack.append(i)
        
    return res

T = [73, 74, 75, 71, 69, 72, 76, 73]
print("Mảng số ngày chờ (Câu 4):", daily_temperatures(T))
# Output: [1, 1, 4, 2, 1, 1, 0, 0]