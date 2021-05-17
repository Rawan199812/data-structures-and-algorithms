# Singly Linked List
Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

## Challenge
Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Within LinkedList class, include a head property. Upon instantiation, an empty Linked List should be created.

## API
1. insert method :  takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
2. includes method: takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
3.  __str__  method: takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
4. kthFromEnd method : Return node value (k) from the end of the list