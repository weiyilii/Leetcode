class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def toMin(t):
            t = map(int, t.split(":"))
            return t[0]*60 + t[1]
        
        t = map(toMin, timePoints)
        t.sort()
        
        return min((y - x)%(24*60) for x, y in zip(t, t[1:] + t[:1]))