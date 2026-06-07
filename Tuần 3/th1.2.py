def bubble_sort (arr):
    for i in range(len(arr)):
        for j in range (len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[123,234,5677,3246576,111,243546,987654,211]
bubble_sort(arr)
print(arr)