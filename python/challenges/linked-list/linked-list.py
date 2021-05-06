class Node(object):
   def _init_ (self,d,n=None):
          self.data = d
          self.next_node = n
   def get_next (self):
          return self.next_node
   def set_next (self,n):
          self.next_node = n
   def get_data (self):
          return self.data
   def set_data (self, d):
            self.data = d

class LinkedList (object):
   def _init_ (self,r=None):
          self.root = r
          self.size = 0
   def insert (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1
   def includes (self, d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None     

myList = LinkedList()
myList.insert(5)
myList.insert(8)
myList.insert(12)
print(myList.includes(5))