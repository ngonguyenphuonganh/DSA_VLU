import math
def check_split(array, max_sum, k):
    pieces = 1
    current_sum = 0
    for num in array:
        if current_sum + num > max_sum:
            pieces = pieces + 1
            current_sum = num
        else:
            current_sum = current_sum + num
    return pieces <= k

def split_array(array, k):
    max_num = array[0]
    total_sum = 0
    for num in array:
        total_sum = total_sum + num
        if num > max_num:
            max_num = num
            
    start = max_num
    end = total_sum
    step = 0
    kq = total_sum
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_split(array, mid, k):
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

array = list(map(int, input("Nhập mảng số: ").split()))
k = int(input("Nhập số k: "))
print("Kết quả:", split_array(array, k))