A = [7, 3, 9, 12, 5, 8, 1]
x = 5
for i in range(len(A)):
    print("Bước", i + 1)
    print("i =", i)
    print("A[i] =", A[i])
    if A[i] == x:
        print("Kết quả: tìm thấy", x)
        print("Vị trí trả về:", i)
        break
    else:
        print("Chưa tìm thấy")
    print()
