def selection_s(arr):
    for index in range (n):
        min_index=index

        for j in range (index+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        (arr[index],arr[min_index])=(arr[min_index],arr[index])
arr =[-25,40,0,15,-90,80,-92,-210,500]
n=len(arr)
selection_s(arr)
print (arr)
    