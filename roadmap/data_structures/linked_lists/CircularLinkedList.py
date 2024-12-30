class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))

circular_llist = CircularLinkedList()
circular_llist.print_list() # None

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
a.next = b
b.next = c
c.next = d
d.next = a
circular_llist.head = a
circular_llist.print_list() # A -> B -> C -> D
circular_llist.print_list(b) # B -> C -> D -> A
circular_llist.print_list(d) # D -> A -> B -> C
