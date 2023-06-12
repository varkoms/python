'''
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are often called push and pop.
'''

'''
Advantages of Stack:

- Stacks are simple data structures with a well-defined set of operations, which makes them easy to understand and use.
- Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1).
- In order to reverse the order of elements we use the stack data structure.
- Stacks can be used to implement undo/redo functions in applications.

Drawbacks of Stack:
- Restriction of size in Stack is a drawback and if they are full, you cannot add any more elements to the stack.
- Stacks do not provide fast access to elements other than the top element.
- Stacks do not support efficient searching, as you have to pop elements one by one until you find the element you are looking for.
'''

# Implementation

# Using lists
stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Using collections.deque
'''
Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

 
The same methods on deque as seen in the list are used, append() and pop().
'''

from collections import deque

stack = deque()

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('\nInitial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# Using LifoQueue module
'''
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 
'''

from queue import LifoQueue

# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print('Full: ', stack.full())
print('Size: ', stack.qsize())

# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())

print('\nEmpty: ', stack.empty())