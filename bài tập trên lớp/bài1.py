def min_truck_capacity(weights, K):
    def can_ship(capacity):
        trucks = 1
        current_load = 0
        for w in weights:
            if current_load + w > capacity:
                trucks += 1
                current_load = w
            else:
                current_load += w
        return trucks <= K
    left = max(weights)
    right = sum(weights)
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_ship(mid):
            ans = mid
            right = mid - 1 
        else:
            left = mid + 1  
            
    return ans

W = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Tải trọng tối thiểu (Câu 1):", min_truck_capacity(W, 5)) 
