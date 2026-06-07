import random

def bubble_sort_count(arr):
    n = len(arr)
    so_sanh = 0
    so_swap = 0

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            so_sanh = so_sanh + 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                so_swap = so_swap + 1
                swapped = True

        if swapped == False:
            break

    return so_sanh, so_swap

n = int(input("Nhap n: "))

mang_da_sap_xep = []
for i in range(1, n + 1):
    mang_da_sap_xep.append(i)

mang_sap_xep_nguoc = []
for i in range(n, 0, -1):
    mang_sap_xep_nguoc.append(i)

mang_ngau_nhien = []
for i in range(1, n + 1):
    mang_ngau_nhien.append(i)

random.shuffle(mang_ngau_nhien)

ss1, sw1 = bubble_sort_count(mang_da_sap_xep.copy())
ss2, sw2 = bubble_sort_count(mang_sap_xep_nguoc.copy())
ss3, sw3 = bubble_sort_count(mang_ngau_nhien.copy())

print("Mang da sap xep:")
print("So sanh:", ss1)
print("So swap:", sw1)

print("Mang sap xep nguoc:")
print("So sanh:", ss2)
print("So swap:", sw2)

print("Mang ngau nhien:")
print("So sanh:", ss3)
print("So swap:", sw3)