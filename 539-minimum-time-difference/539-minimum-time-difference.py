class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def timeDiff(t1, t2):
            t1 = map(int, t1.split(':'))
            t2 = map(int, t2.split(':'))
            diff1 = (t2[0] - t1[0])*60 + t2[1] - t1[1]
            diff2 = t1[0]*60 + t1[1] + (24 - t2[0])*60 - t2[1]
            return min(diff1, diff2)
        
        timePoints.sort()
        res = 24*60
        for i in range(1, len(timePoints)-1):
            res = min(res, timeDiff(timePoints[i-1], timePoints[i]),
                      timeDiff(timePoints[i], timePoints[i+1]))
        res = min(res, timeDiff(timePoints[0], timePoints[len(timePoints)-1]))
        return res