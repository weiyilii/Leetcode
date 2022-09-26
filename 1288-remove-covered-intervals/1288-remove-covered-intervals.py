class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = len(intervals)
        intervals.sort(key = lambda x: (x[0], -x[1]))
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            end = intervals[i][1]
            if end <= right:
                res -= 1
            else:
                right = end
        return res