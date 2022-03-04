"""
Binary tree
tree represents the nodes connected by edges. it is a non
linear data structure.
one node marked as root node
every node other than root is associated with one parent node
each node can have an arbitrary number of chile node

in binary left is smaller than root and right is bigger
than root
"""

# create root
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        print(self.data)

root = Node(10)
# root.printTree()

# inserting into a tree
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertData(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertData(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertData(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

root = Node(12)
root.insertData(6)
root.insertData(90)
root.insertData(3)
root.insertData(8)
root.printTree()