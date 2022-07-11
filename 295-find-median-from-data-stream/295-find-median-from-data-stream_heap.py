class MedianFinder(object):
    
    from heapq import heappush, heappushpop

    def __init__(self):
        self.s = []
        self.l = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.s) < len(self.l):
            if num < self.l[0]:
                heappush(self.s, -num)
            else:
                temp = heappushpop(self.l, num)
                heappush(self.s, -temp)
        else:
            if len(self.l) == 0 or num > -self.s[0]:
                heappush(self.l, num)
            else:
                temp = heappushpop(self.s, -num)
                heappush(self.l, -temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.s) < len(self.l):
            return self.l[0]
        else:
            return float(-self.s[0] + self.l[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
