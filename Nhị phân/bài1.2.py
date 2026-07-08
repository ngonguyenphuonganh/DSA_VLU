import math
def binary_search(array, element):
   mid=0
   left = 0
   right=len(array)
   end = len(array)
   step = 0
   while (left<=right):
      step = step+1
      mid = (left + right) // 2

      if(element==array[mid]):
         return mid
      elif (element<array[mid]):
         right=mid-1
      else :
         left=mid+1
   return -1
array=list(map(int, input("Nhập mảng số bạn muốn:").split()))
element=int(input("Nhập số:"))
kq=binary_search(array, element)
print("Vị trí tìm kiếm là:",kq)
