import math
def check_books(pages, max_pages, students):
    allocated = 1
    current = 0
    for p in pages:
        if current + p > max_pages:
            allocated = allocated + 1
            current = p
        else:
            current = current + p
    return allocated <= students

def allocate_books(pages, m):
    if m > len(pages):
        return -1
    max_p = pages[0]
    total_p = 0
    for p in pages:
        total_p = total_p + p
        if p > max_p:
            max_p = p
            
    start = max_p
    end = total_p
    step = 0
    kq = total_p
    while (start <= end):
        step = step + 1
        mid = (start + end) // 2
        if check_books(pages, mid, m):
            kq = mid
            end = mid - 1
        else:
            start = mid + 1
    return kq

pages = list(map(int, input("Nhập số trang: ").split()))
m = int(input("Nhập số học sinh m: "))
print("Số trang lớn nhất tối thiểu:", allocate_books(pages, m))