class SummaryRanges(object):
    
    from heapq import heappush, heappop
    
    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.seen:
            self.seen.add(val)
            heappush(self.intervals, [val, val])

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        tmp = []
        while self.intervals:
            cur = heappop(self.intervals)
            if tmp and cur[0] <= tmp[-1][1] + 1:
                tmp[-1][1] = max(cur[1], tmp[-1][1])
            else:
                tmp.append(cur)
        self.intervals = tmp
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()