class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        n = len(machines)
        s = sum(machines)
        if s % n != 0:
            return -1
        k = s/n
        
        left = [0]*n
        right = [0]*n
        
        right[0] = machines[0] - k
        left[n-1] = machines[n-1] - k
        
        for i in range(1, n-1):
            left[i] = -right[i-1]
            right[i] = machines[i] - k - left[i]
            
        res = 0
        for i in range(n):
            t = 0
            if left[i] >= 0:
                t += left[i]
            if right[i] >= 0:
                t += right[i]
            res = max(res, t)
        
        return res