def group_by(arr):
    groups = {}
    for word in arr:
        first_char = word[0]
        if first_char not in groups:
            groups[first_char] = []
        groups[first_char].append(word)
    return groups