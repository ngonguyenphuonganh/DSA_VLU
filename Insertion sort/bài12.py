def sort_by_length(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and len(a[j]) > len(key):
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(sort_by_length(['abc', 'a', 'ab'])) # Output: ['a', 'ab', 'abc']