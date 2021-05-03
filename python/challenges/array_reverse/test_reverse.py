from array_reverse import reverseArray





arr = [1, 2, 3, 4, 5, 6]
expected = [6, 5, 4, 3, 2, 1]
# Assign
actual  =  reverseArray(arr)
# Assert
if expected == actual:
    print('True')
else:
    print('False')
assert expected == actual

