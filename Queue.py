"""
::::::QUEUE:::::::
FIFO = First In First Out
it can be implemented using insert and pop operation
"""

# adding in a queue

class queue:
    def __init__(self):
        self.queue = list()

    def addToQ(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        else:
            return False

    def size(self):
        return len(self.queue)

theQ = queue()
theQ.addToQ('mon')
theQ.addToQ('tue')
theQ.addToQ('mon')
print(theQ.size())

print('--------------------')
# removing element from a queue

class queue:
    def __init__(self):
        self.queue = list()

    def addToQ(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        else:
            return False

    def removeFromQ(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return 'queue is empty!'

    def size(self):
        return len(self.queue)
theQ = queue()
theQ.addToQ('mon')
theQ.addToQ('tue')
theQ.addToQ('wed')
print(theQ.removeFromQ())
print(theQ.size())
print(theQ.removeFromQ())
print(theQ.size())