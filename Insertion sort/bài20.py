def count_shifts_large(a):
    # Đếm nghịch thế bằng Merge Sort O(n log n)
    def merge_sort_count(arr):
        if len(arr) <= 1: return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort_count(arr[:mid])
        right, inv_right = merge_sort_count(arr[mid:])
        merged, inv_split = merge(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
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
        merged += left[i:]
        merged += right[j:]
        return merged, inv

    _, total_shifts = merge_sort_count(a)
    return total_shifts