class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.size = maxSize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.size > 0:
            self.stack.append(x)
            self.size -= 1

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            self.size += 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)