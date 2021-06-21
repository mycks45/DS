def selection_sort(arr):
    length = len(arr)
    i = 0
    while i < (length-1):
        j = i+1
        while j<length:
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            j +=1
        i +=1
    return arr

arr = [5,3,78,212,43,12,34,23,56,32,41,45,24,64,57,97,35]

print(arr)
result = selection_sort(arr)
print(result)