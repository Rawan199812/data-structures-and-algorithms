# from array_binary_search import __version__
from array_binary_search import BinarySearch


# def test_version():
#     assert __version__ == '0.1.0'


def test_one():
    actual = BinarySearch([10, 20, 30, 40], 20)
    expected = 1
    assert actual == expected


def test_element_does_not_exist():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

def test_two():
    actual = BinarySearch([4,8,15,16,23,42], 23)
    expected = 4
    assert actual == expected