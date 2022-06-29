class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [0]*k
        self.max_size = k
        self.size = 0
        self.front, self.rear = -1, -1

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front-1) % self.max_size
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
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

    def deleteFront(self):
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

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.size == 1:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear-1) % self.max_size
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        return self.q[self.front] if not self.isEmpty() else -1

    def getRear(self):
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

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()