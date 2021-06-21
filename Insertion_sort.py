def insertion_sort(arr):
    length = len(arr)
    i = 1
    while i < length:
        anchor = arr[i]
        j = i -1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = anchor
        i += 1
    return arr

arr = [12,43,12,34,23,56,32,41,45,24,64,57,97,35]

print(arr)
result = insertion_sort(arr)
print(result)