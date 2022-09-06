class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack) < 1:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if len(self.inc) > 0:
            self.inc[min(k, len(self.inc)) - 1] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)