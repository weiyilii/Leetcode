class MinStack(object):

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.main_stack.append(val)
        if len(self.min_stack) < 1 or self.min_stack[-1] > val:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        """
        :rtype: None
        """
        self.min_stack.pop()
        return self.main_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.main_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()