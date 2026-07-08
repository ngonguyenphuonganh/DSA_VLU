import random
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
n = 100
best = list(range(n))
worst = list(range(n, 0, -1))
avg = best.copy()
random.shuffle(avg)
print("Best shifts:", count_shifts(best))
print("Worst shifts:", count_shifts(worst))
print("Avg shifts:", count_shifts(avg))
