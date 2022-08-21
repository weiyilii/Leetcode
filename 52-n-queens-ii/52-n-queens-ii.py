class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        
        def dfs(q):
            i = len(q)
            if i == n:
                self.res += 1
                return
            for j in range(n):
                if self.isValid(q, i, j):
                    dfs(q + [j])
        
        dfs([])
        return self.res
    
    def isValid(self, q, i, j):
        for x, y in enumerate(q):
            if y == j or x + y == i + j or x - y == i - j:
                return False
        return True