def longest_consecutive(arr):
    num_set = set(arr)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr = num
            length = 1
            while curr + 1 in num_set:
                curr += 1
                length += 1
            max_length = max(max_length, length)
    return max_length