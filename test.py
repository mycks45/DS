

def swap(arr):
    arr[0],arr[-1] = arr[-1],arr[0]
    return arr

def multiple(arr):
    res = 1
    for i in arr:
        res = res * i
    return res

def findMinValues(arr):
    arr.sort()
    return arr[0]

def findEven(arr):
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
    return even

def findOdd(arr):
    odd = []
    for i in arr:
        if i % 2 == 1:
            odd.append(i)
    return odd

arr = [12,23,54,34,23,78,4,6,8,75,6,3,5,7]
# print(swap(arr))
# arr.pop()

# arr = multiple(arr)
# arr = findMinValues(arr)
# arr = findOdd(arr)
# arr = findEven(arr)

print(arr)