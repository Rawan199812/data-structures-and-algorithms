def insertShiftArray(arr,value):
    for x in range(len(arr)):
        if arr[x] > value:
            i = x
            break
    arr = arr[:x] + [value] + arr[x:]
    return arr
    
