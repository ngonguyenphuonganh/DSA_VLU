def find_intersection(arr1, arr2):
    hash_set = set(arr1)
    result = []
    for item in arr2:
        if item in hash_set:
            result.append(item)
            hash_set.remove(item)
    return result