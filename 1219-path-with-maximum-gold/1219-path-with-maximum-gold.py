class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            ans = 0
            gold = grid[i][j]
            grid[i][j] = 0
            d_i = [-1, 1, 0, 0]
            d_j = [0, 0, -1, 1]
            for k in range(4):
                ans = max(ans, dfs(i + d_i[k], j + d_j[k]))
            grid[i][j] = gold
            return gold + ans
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    res = max(res, dfs(i, j))
        return res