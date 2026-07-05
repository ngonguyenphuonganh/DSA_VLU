def remove_duplicates_o_n2(arr):
    result = []
    for item in arr:
        if item not in result:
            result.append(item)
    return result

def remove_duplicates_o_n(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result