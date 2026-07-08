def max_sliding_window(nums, k):
    q = []
    res = []
    for i, n in enumerate(nums):
        while q and q[0] < i - k + 1:
            q.pop(0)
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res