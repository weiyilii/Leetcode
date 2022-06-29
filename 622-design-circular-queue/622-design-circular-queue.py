class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0]*k
        self.front, self.rear = -1, -1
        self.max_size = k
        self.size = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1) % self.max_size
        self.q[self.rear] = value
        self.size += 1  
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front+1) % self.max_size
        self.size -= 1
        return True

    def Front(self):
        """
        :rtype: int
        """
        return self.q[self.front] if not self.isEmpty() else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.q[self.rear] if not self.isEmpty() else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.max_size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()