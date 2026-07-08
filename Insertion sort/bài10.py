def check_shifts_vs_inversions(a):
    inversions = sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])
    shifts = count_shifts(a.copy())
    return f"Nghịch thế: {inversions}, Shifts: {shifts}"

print(check_shifts_vs_inversions([2, 4, 1, 3]))
def count_shifts(a):
    shifts = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1

        a[j + 1] = key

    return shifts
