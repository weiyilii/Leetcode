class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i, j = 0, 0
        g.sort()
        s.sort()
        res = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1
        
        return res