from array_reverse import reverse_list





arr = [1, 2, 3, 4, 5, 6]
expected = [6, 5, 4, 3, 2, 1]
# Assign
actual  =  reverse_list(arr)
# Assert
if expected == actual:
    print('True')
else:
    print('False')
assert expected == actual

# def test_leave_as_is():
#     actual = reverse_list([1])
#     expected = [1]
#     assert actual == expected
# def test_revers():
#     actual = reverse_list([1])
#     expected = [1]
#     assert actual == expected
