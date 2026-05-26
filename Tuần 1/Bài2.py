def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
a = [7, 3, 9, 12, 5, 8, 1]
x = 5
ket_qua = linear_search(a, x)
print("Vị trí:", ket_qua)

#Input:
#Mảng a
#Giá trị cần tìm x
#Output:
#Vị trí của x trong mảng
#Nếu không có → -1