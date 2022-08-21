class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(path, curSum):
            l = len(path)
            if l == k:
                if curSum == n:
                    res.append(path)
                return
            start = path[-1] + 1 if path else 1
            end = min(n, 10)
            for i in range(start, end):
                dfs(path + [i], curSum + i)
        
        dfs([], 0)
        return res