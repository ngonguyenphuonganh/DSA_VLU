def match_2d(matrix, pattern):
    R, C = len(matrix), len(matrix[0])
    r, c = len(pattern), len(pattern[0])
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            if all(matrix[i + kr][j:j + c] == pattern[kr] for kr in range(r)):
                return (i, j)
    return -1