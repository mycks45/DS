def bubbleSort(arr):
    lenght = len(arr)

    i = 0
    while i < lenght-1:
        j = 0
        while j < (lenght-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            j += 1
        i += 1

    return arr

arr = [45,34,54,76,34,76,98,34,56,90,23,2,34,23,34,54]

print(arr)
result = bubbleSort(arr)
print(result)
