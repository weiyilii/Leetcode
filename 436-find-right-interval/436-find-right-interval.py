class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        if n == 1:
            return [-1]
        
        res = [-1]*n
        
        interval_index = [[s, e, i] for i, [s, e] in enumerate(intervals)]
        interval_index.sort()
        
        for k in range(n):
            end, i = interval_index[k][1], interval_index[k][2]
            left, right = k, n
            while left < right:
                mid = left + (right-left)//2
                if interval_index[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1
            if left != n:
                res[i] = interval_index[left][2]
        return res
            