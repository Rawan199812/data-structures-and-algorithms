
def BinarySearch(s_list, key):

    if len(s_list) > 0:
           mid = len(s_list) // 2
    
           if s_list[mid] == key:
               return mid
    
           if key < s_list[mid]:
               return BinarySearch(s_list[:mid], key)
    
           if key > s_list[mid]:
               return BinarySearch(s_list[mid + 1:], key)
    
    else:
        return -1

    