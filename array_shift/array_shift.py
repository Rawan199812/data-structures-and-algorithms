def insertShiftArray(arr,value):
    for y in range(len(arr)):
        if arr[y] > value:
            i = y
            break
    arr = arr[:y] + [value] + arr[y:]
    return arr