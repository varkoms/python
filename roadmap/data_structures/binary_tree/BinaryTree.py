class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insert(root, new_value):
    if root is None:
        root = BinaryTreeNode(new_value)
        return root
    if new_value < root.data:
        root.leftchild = insert(root.leftchild, new_value)
    else:
        root.rightchild = insert(root.rightchild, new_value)
    return root


def search(root, value):
    if root is None:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search(root.leftchild, value)
    else:
        return search(root.rightchild, value)

# Creating a binary tree
root = insert(None, 50)

# Inserting values into the tree
insert(root, 20)
insert(root, 53)
insert(root, 11)
insert(root, 22)
insert(root, 52)
insert(root, 78)
# Traversing the tree
node1 = root
node2 = node1.leftchild
node3 = node1.rightchild
node4 = node2.leftchild
node5 = node2.rightchild
node6 = node3.leftchild
node7 = node3.rightchild

# Printing the tree
print("Root Node is:")
print(node1.data)

print("left child of the node is:")
print(node1.leftchild.data)

print("right child of the node is:")
print(node1.rightchild.data)

print("Node is:")
print(node2.data)

print("left child of the node is:")
print(node2.leftchild.data)

print("right child of the node is:")
print(node2.rightchild.data)

print("Node is:")
print(node3.data)

print("left child of the node is:")
print(node3.leftchild.data)

print("right child of the node is:")
print(node3.rightchild.data)

print("Node is:")
print(node4.data)

print("left child of the node is:")
print(node4.leftchild)

print("right child of the node is:")
print(node4.rightchild)

print("Node is:")
print(node5.data)

print("left child of the node is:")
print(node5.leftchild)

print("right child of the node is:")
print(node5.rightchild)

print("Node is:")
print(node6.data)

print("left child of the node is:")
print(node6.leftchild)

print("right child of the node is:")
print(node6.rightchild)

print("Node is:")
print(node7.data)

print("left child of the node is:")
print(node7.leftchild)

print("right child of the node is:")
print(node7.rightchild)

# Searching for a value in the tree
print("Searching for 22 in the tree:", search(root, 22))
print("Searching for 100 in the tree:", search(root, 100))
