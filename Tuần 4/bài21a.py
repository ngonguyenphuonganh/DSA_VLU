def is_21(arr):
    def merge_sort_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_left = merge_sort_count(a[:mid])
        right, inv_right = merge_sort_count(a[mid:])
        merged, inv_merge = merge_count(left, right)
        return merged, inv_left + inv_right + inv_merge

    def merge_count(left, right):
        merged = []
        inv = 0
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, inv = merge_sort_count(arr)
    return inv