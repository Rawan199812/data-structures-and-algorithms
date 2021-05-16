import pytest
from linked_list import Node, LinkedList
myList = LinkedList()


# def test_import():
#     assert LinkedList

# def test_import():
#     assert Node

def add_to_the_end():
    myList.append('test')
    actual = myList.includes('test')
    expected = True
    assert actual == expected
@pytest.fixture
def linked():
    item = LinkedList()
    item.insert('Rawan')
    item.insert('12')
    item.insert('so')
    item.insert('cool')
    item.insert('yes')



    return item