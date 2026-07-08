a = []
stream = [5, 2, 8, 1]
for x in stream:
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i] < a[i - 1]:
        a[i], a[i - 1] = a[i - 1], a[i]
        i -= 1
    print(a)