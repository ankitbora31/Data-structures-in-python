"""
a BST is a tree in which all the nodes follow the below
mentioned properties - the left sub tree of a node has a
key less than or equal to its parent node's key. the right
sub tree of a node has a key greater than to its parent node's
key.
left_subtree(keys)<=node(key)<=right_subtree(keys)
"""

# searching for a value in binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_val(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" not found"
            return self.left.find_val(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " not found"
            return self.right.find_val(val)
        else:
            print(str(self.data) + " is found")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(6)
root.insert(8)
root.insert(14)
print(root.find_val(4))
print(root.find_val(8))