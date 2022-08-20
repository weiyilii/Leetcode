class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(path):
            if len(path) == k:
                res.append(path)
            start = path[-1]
            for i in range(start+1, n+1):
                dfs(path + [i])
        
        for i in range(1, n+1):
            dfs([i])
        
        return res