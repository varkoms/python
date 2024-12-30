from collections import deque

print(deque(['a', 'b', 'c']))
print(deque('abc'))

llist = deque('abcde')
print(llist)

llist.append('f')
print(llist)

llist.pop()
print(llist)

llist.appendleft('z')
print(llist)

llist.popleft()
print(llist)

# Practical example
personas = deque()
print(personas)

"""
With queues, you want to add values to a list (enqueue), and when the timing is right, you want to remove the element that has been on the list the longest (dequeue). For example, imagine a queue at a trendy and fully booked restaurant. If you were trying to implement a fair system for seating guests, then you’d start by creating a queue and adding people as they arrive:
"""
personas.append('Mary')
personas.append('John')
personas.append('Susan')
print(personas)

"""
Now you have Mary, John, and Susan in the queue. Remember that since queues are FIFO, the first person who got into the queue should be the first to get out.

Now imagine some time goes by and a few tables become available. At this stage, you want to remove people from the queue in the correct order. This is how you would do that:
"""
personas.popleft()
print(personas) # deque(['John', 'Susan'])

personas.popleft()
print(personas) # deque(['Susan'])

