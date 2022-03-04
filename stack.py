"""
stack means arranging objects on over another.
we can add or delete elements at only one end of the
stack called at the top of stack
LIFO = last In First Out
adding = push
removing = pop
"""

# PUSH into a stack

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # using list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # using peek to look at top of the stack
    def peek(self):
        return self.stack[-1]

aStack = Stack()
aStack.add('Mon')
aStack.add('Tue')
print('at top after adding mon and tue: {}'.format(aStack.peek()))
aStack.add('wed')
aStack.add('thu')
print('at top after adding wed and thu: {}'.format(aStack.peek()))


print('-----------------------------------')
# POP from a stack

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    def remove(self):
        if len(self.stack) <= 0:
            return 'no element in the stack'
        else:
            return self.stack.pop()

aStack = Stack()
aStack.add('Mon')
aStack.add('Tue')
print(aStack.remove())
aStack.add('wed')
aStack.add('thu')
print(aStack.remove())