a = [1, 3, 2, 5, 4, 6]
shift = 0
for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        shift += 1
        j -= 1
    a[j + 1] = key
print("Mảng đã sắp xếp:", a)
print("Số shift:", shift)