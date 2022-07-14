class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # In Python, the remainder will be the same sign as the denominator (the divisor)
        # -3 % 2 = (-2*2 + 1) % 2 = 1
        
        def toMin(t):
            t = map(int, t.split(":"))
            return t[0]*60 + t[1]
        
        t = map(toMin, timePoints)
        t.sort()
        
        return min((y - x)%(24*60) for x, y in zip(t, t[1:] + t[:1]))
