def binarySearch(number_list, item):

    left_index = 0 
    right_index = len(number_list)-1
    middle_index = 0

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        middle_number = number_list[middle_index]

        if middle_number == item:
            return middle_index
        
        if middle_number < item:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    
    return 'Not in the arr'

number_list = [1,2,3,4,5,6,12,23,34,45,56,67,78,89]
item =78

result = binarySearch(number_list, item)
print('Index of the item is ',result)