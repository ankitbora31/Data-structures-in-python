"""
in the prev linked list we did singly linked list.
now in this we doing doubly linked list which can travel
both backward and forward.
each node carries one data and 2 pointer fields.
one pointer points to prev and other to next node.
The last link carries a link as NULL to mark the end of
the list.
"""


# creating a doubly linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # adding data elements
    def push(self, newVal):
        newNode = Node(newVal)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    # print the doubly linked list
    def listprint(self, node):
        while node is not None:
            print(node.data),
            last = node
            node = node.next


dLL = DoublyLL()
dLL.push(12)
dLL.push(20)
dLL.push(18)
dLL.listprint(dLL.head)

print('--------------------------')


# inserting into DLL

# Create the Node class


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create the doubly linked list


class doubly_linked_list:

    def __init__(self):
        self.head = None

    # Define the push method to add elements
    def push(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Define the insert method to insert the element
    def insert(self, prev_node, NewVal):
        if prev_node is None:
            return
        NewNode = Node(NewVal)
        NewNode.next = prev_node.next
        prev_node.next = NewNode
        NewNode.prev = prev_node
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    # Define the method to print the linked list
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


dLL = doubly_linked_list()
dLL.push(12)
dLL.push(8)
dLL.push(62)
dLL.insert(dLL.head.next, 13)
dLL.listprint(dLL.head)

print('----------------------------')


# appending to a doubly linked list
# Create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Create the doubly linked list class
class doubly_linked_list:

    def __init__(self):
        self.head = None

    # Define the push method to add elements at the begining
    def push(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    # Define the append method to add elements at the end
    def append(self, NewVal):

        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            return
        last = self.head
        while (last.next is not None):
            last = last.next
        last.next = NewNode
        NewNode.prev = last
        return

    # Define the method to print
    def listprint(self, node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next


dLL = doubly_linked_list()
dLL.push(12)
dLL.append(9)
dLL.push(8)
dLL.push(62)
dLL.append(45)
dLL.listprint(dLL.head)
