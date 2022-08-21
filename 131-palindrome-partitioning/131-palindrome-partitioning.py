class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        n = len(s)
        
        def dfs(path, prev):
            if prev == n-1:
                res.append(path)
            for i in range(prev + 1, n):
                sub = s[prev+1:i+1]
                if sub == sub[::-1]:
                    dfs(path + [sub], i)
        
        dfs([], -1)
        return res