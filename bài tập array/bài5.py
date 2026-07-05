def traverse_and_count_even(arr):
    count = 0
    for item in arr:
        print(item, end=" ")
        if item % 2 == 0:
            count += 1
    print()
    return count