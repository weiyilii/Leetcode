class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        end = float('-inf')
        res = 0
        intervals.sort(key = lambda x: x[1])
        for interval in intervals:
            s = interval[0]
            e = interval[1]
            if s >= end:
                end = e
            else:
                res += 1
        return res