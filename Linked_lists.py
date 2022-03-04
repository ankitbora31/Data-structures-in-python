"""
A linked list is a sequence of data elements which are
connected together via links. each data element contains
a connection to another data element in form of a pointer.
python does not include linked lists in its standard
library.
"""

# creation of a linked list

#
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# # link first node to second node
# list1.headval.nextval = e2
#
# # link second node to third node
# e2.nextval = e3
#
# print('---------------------------')
# """
# traversal of a linked list
# """
#
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
#     # print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# list1.headval.nextval = e2
# e2.nextval = e3
#
# list1.listprint()
#
# print('---------------------------')
# """
# insertion in linked list at beginning
# """
#
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
#     # print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval
#
#     def AtBeginning(self, newdata):
#         NewNode = Node(newdata)
#
#         # update the new nodes next val to existing node
#         NewNode.nextval = self.headval
#         self.headval = NewNode
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# list1.headval.nextval = e2
# e2.nextval = e3
#
# list1.AtBeginning('sun')
# list1.listprint()
#
# print('---------------------------')
#
#
# # insertion at the end of the linked list
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
#     # function to add new node at end
#     def AtEnd(self, newdata):
#         NewNode = Node(newdata)
#         if self.headval is None:
#             self.headval = NewNode
#             return
#         laste = self.headval
#         while(laste.nextval):
#             laste = laste.nextval
#         laste.nextval = NewNode
#
#     # print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# list1.headval.nextval = e2
# e2.nextval = e3
#
# list1.AtEnd('Thu')
# list1.listprint()
#
# print('---------------------------')
#
# # insertion between two nodes
#
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None
#
#
# class SLinkedList:
#     def __init__(self):
#         self.headval = None
#
#     # function to add new node at end
#     def InBetween(self, middle_node, newdata):
#         if middle_node is None:
#             print('the mentioned node is absent')
#             return
#
#         NewNode = Node(newdata)
#         NewNode.nextval = middle_node.nextval
#         middle_node.nextval = NewNode
#
#     # print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print(printval.dataval)
#             printval = printval.nextval
#
# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node('Tue')
# e3 = Node('Wed')
#
# list1.headval.nextval = e2
# e2.nextval = e3
#
# list1.InBetween(list1.headval.nextval, 'Fri')
# list1.listprint()
#
# print('---------------------------')
#
# # removing an item from a linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Slinkedlist:
    def __init__(self):
        self.head = None

    def Atbeginning(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

    # function to remove node

    def RemoveNode(self, Remove_key):
        HeadVal = self.head
        if HeadVal is not None:
            if HeadVal.data == Remove_key:
                self.head = HeadVal.next
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.data == Remove_key:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if HeadVal == None:
            return

        prev.next = HeadVal.next

        HeadVal = None

    def listprint(self):
        printval = self.head
        while(printval):
            print(printval.data)
            printval = printval.next

llist = Slinkedlist()
llist.Atbeginning('mon')
llist.Atbeginning('tue')
llist.Atbeginning('wed')
llist.Atbeginning('thu')
llist.RemoveNode('wed')
llist.listprint()