class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])
        pacific = [[False for j in range(n)] for i in range(m)]
        atlantic = [[False for j in range(n)] for i in range(m)]
        res = []
        for i in range(m):
            self.dfs(i, 0, float('-inf'), heights, pacific)
            self.dfs(i, n-1, float('-inf'), heights, atlantic)
        for j in range(n):
            self.dfs(0, j, float('-inf'), heights, pacific)
            self.dfs(m-1, j, float('-inf'), heights, atlantic)
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
    
    def dfs(self, i, j, h, heights, dp):
        if i < 0 or i >= len(dp) or j < 0 or j >= len(dp[0]) or dp[i][j] or heights[i][j] < h:
            return
        dp[i][j] = True
        h = heights[i][j]
        self.dfs(i-1, j, h, heights, dp)
        self.dfs(i+1, j, h, heights, dp)
        self.dfs(i, j-1, h, heights, dp)
        self.dfs(i, j+1, h, heights, dp)