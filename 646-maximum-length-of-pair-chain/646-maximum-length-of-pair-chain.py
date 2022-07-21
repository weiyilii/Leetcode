class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda x: x[1])
        cur, res = float('-inf'), 0
        
        for (x, y) in pairs:
            if cur < x:
                cur = y
                res += 1
        
        return res