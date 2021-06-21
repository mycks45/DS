# time complexity of the merge sort is O(n log n)


def mergeSort(array):

    if len(array)>1:
        
        middleIdx = len(array)//2
        leftHalf = array[:middleIdx]
        rightHalf = array[middleIdx:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)


        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                array[k] = leftHalf[i]
                i += 1
            else:
                array[k] = rightHalf[j]
                j += 1
            k += 1

        while i  < len(leftHalf):
            array[k] = leftHalf[i]
            i += 1 
            k += 1

        while j  < len(rightHalf):
            array[k] = rightHalf[j]
            k += 1
            j += 1 
    
    return array


a = [30,2,41,56,12,11,22,41]
result = mergeSort(a)
print(result)