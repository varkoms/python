'''
Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element. 
'''
# Linked List implementation in Python

# Creating a node
class Node:
    def __init__(self):
        self.value = 0
        self.next = None

head = None
one = None
two = None
three = None

# allocate 3 nodes in the heap
one = Node()
two = Node()
three = Node()

# Assing value values
one.value = 1
two.value = 2
three.value = 3

# Connect nodes
one.next = two
two.next = three
three.next = None

# print the linked list value
head = one

while (head != None):
    print(head.value) # Output: 123
    head = head.next
