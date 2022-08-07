class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        
        def dfs(i, j):
            # if dp[i][j] == 0: this has not been visited
            # after visiting, dp[i][j] >= 1
            # if this has been visited, just return
            if not dp[i][j]:
                cur = matrix[i][j]
                move = [0]*4
                if i-1 >= 0 and matrix[i-1][j] > cur:
                    move[0] = dfs(i-1, j)
                if i+1 < m and matrix[i+1][j] > cur:
                    move[1] = dfs(i+1, j)
                if j-1 >= 0 and matrix[i][j-1] > cur:
                    move[2] = dfs(i, j-1)
                if j+1 < n and matrix[i][j+1] > cur:
                    move[3] = dfs(i, j+1)
                dp[i][j] = 1 + max(move)
            return dp[i][j]
        
        res = float('-inf')
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res