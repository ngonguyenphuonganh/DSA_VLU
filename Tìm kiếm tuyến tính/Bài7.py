def linear_search(n, x):
    for i in range(len(n)):
        if n[i] == x:
            return i
    return -1
a = list(map(int, input("Nhập mảng: ").split()))
x = int(input("Nhập số cần tìm: "))
ket_qua = linear_search(a, x)
print("Kết quả:", ket_qua)