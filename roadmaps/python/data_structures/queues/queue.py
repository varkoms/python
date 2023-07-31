'''
Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner. With a queue the least recently added item is removed first. A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.
'''

# IMPLEMENTATIONS
'''
There are various ways to implement a queue in Python. This article covers the implementation of queue using data structures and modules from Python library.
Queue in Python can be implemented by the following ways:
 
- list
- collections.deque
- queue.Queue
'''

# Implementation using lists

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print('Initial queue')
print(queue)

# Removing elements from the queue
print('\nElements dequeued from queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nElements after removing elements')
print(queue)

# Implementation using collections.deque
'''
Queue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Instead of enqueue and deque, append() and popleft() functions are used.
'''

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print('\nInitial Queue')
print(q)

# Removing elements from a queue
print('\nElements dequeued from the queue')
print(q.popleft())
print(q.popleft())
print(q.popleft())

print('\nQueue after removing elements')
print(q)