
def BinarySearch(s_list, key):

    last_index = len(s_list) - 1
    first_index = 0
 
    while first_index <= last_index:
 
        middle_index = (last_index + first_index) // 2
 
        if s_list[middle_index] > key:
            last_index = middle_index - 1
 
        elif s_list[middle_index] < key:
            first_index = middle_index + 1

        else:
            return middle_index
 
    return -1
