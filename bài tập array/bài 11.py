def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n

    def reverse_sub(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    reverse_sub(0, n - 1)
    reverse_sub(0, k - 1)
    reverse_sub(k, n - 1)
    return arr