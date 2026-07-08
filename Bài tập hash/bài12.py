def count_subarrays(arr, k):
    prefix_map = {0: 1}
    current_sum = 0
    count = 0
    for num in arr:
        current_sum += num
        count += prefix_map.get(current_sum - k, 0)
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
    return count