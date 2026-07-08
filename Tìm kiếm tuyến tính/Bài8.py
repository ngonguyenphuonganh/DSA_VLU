def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False
a = list(map(int, input("Nhập mảng: ").split()))
x = int(input("Nhập số cần kiểm tra: "))
print(ton_tai(a, x))