def double_selection_with_counts(a):
    n = len(a)
    left, right = 0, n - 1
    comps = 0
    swaps = 0

    while left < right:
        min_i = left
        max_i = left

        for i in range(left, right + 1):
            comps += 1
            if a[i] < a[min_i]:
                min_i = i
            comps += 1
            if a[i] > a[max_i]:
                max_i = i

        if min_i != left:
            a[left], a[min_i] = a[min_i], a[left]
            swaps += 1

        if max_i == left:
            max_i = min_i

        if max_i != right:
            a[right], a[max_i] = a[max_i], a[right]
            swaps += 1

        left += 1
        right -= 1

    return a, comps, swaps