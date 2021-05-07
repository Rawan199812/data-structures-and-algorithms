# class LinkedLists:
#     """
#     Put docstring here
#     """

#     def __init__(self):
#         # initialization here
#         pass

#     def some_method(self):
#         # method body here
#         pass
class Node():

    def __init__ (self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next (self):
        return self.next_node

    def get_data (self):
        return self.data


class LinkedList ():

    def __init__(self, h = None):
        self.head = h
        self.size = 0

    def insert (self, d):
        new_node = Node (d, self.head)
        self.head = new_node
        self.size += 1
        return new_node.data

    def includes (self, d):
        this_node = self.head
        while this_node:
            if this_node.get_data() == d:
                return True
            else:
                this_node = this_node.get_next()
        return False
    def __str__(self):
        if self.head:
            saved_data = "{"f"{self.head.data}""} "
            this_node = self.head
            while this_node:
                this_node = this_node.next_node
                if  this_node:
                    saved_data += "-> ""{"f"{ this_node.data}""} "
                else:
                    saved_data += "-> NULL"
        else:
            return "Your List still empty"
        return saved_data
# myList = LinkedList()
# myList.insert(5)
# myList.insert(8)
# myList.insert(12)

# print(myList.includes(5))
# print(myList.includes(3))
# print(myList.__str__())
