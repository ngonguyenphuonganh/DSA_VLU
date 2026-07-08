def subarray_sum(nums, S):
    prefix_counts = {0: 1} # Khởi tạo: Có 1 cách để tạo ra tổng bằng 0
    curr_sum = 0
    count = 0
    
    for num in nums:
        curr_sum += num
        # Kiểm tra xem có tiền tố nào thỏa mãn: curr_sum - (tiền tố) = S không
        target = curr_sum - S
        if target in prefix_counts:
            count += prefix_counts[target]
            
        # Lưu tổng cộng dồn hiện tại vào bảng băm
        prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
        
    return count

A_7 = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7
print("Số mảng con có tổng bằng 7 (Câu 7):", subarray_sum(A_7, S))
# Output: 4