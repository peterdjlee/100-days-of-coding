import random

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)

def insert(root, node):
    if node.value < root.value:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)
    if node.value > root.value:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

def find(root, key):
    if root is None or root.value == key:
        return root
    if key < root.value:
        return find(root.left, key)
    if key > root.value:
        return find(root.right, key)

def printBST(node):
    if node is None:
        return
    else:
        printBST(node.left)
        print(node.value)
        printBST(node.right)

root = Node(8)

insert(root, Node(9))
insert(root, Node(10))
insert(root, Node(7))
insert(root, Node(6))

for i in range(100000):
    insert(root, Node(random.randint(1,10000000)))

# printBST(root)

print(find(root, 9))