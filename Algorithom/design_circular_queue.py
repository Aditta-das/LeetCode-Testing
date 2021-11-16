class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.queue = []

    def enQueue(self, value):
        if self.isFull():
            return False
        self.queue.append(value)
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty(): return False
        self.queue.pop(0)
        return True
        

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[0]
        

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if not self.queue:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if len(self.queue) == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_2 = obj.enQueue(2)
param_3 = obj.enQueue(3)
param_4 = obj.enQueue(4)
param_5 = obj.enQueue(5)
print(param_1, param_2, param_3, param_4, param_5)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()