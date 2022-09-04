class Solution(object):
    def knightProbability(self, n, k, row, column):
        """
        :type n: int
        :type k: int
        :type row: int
        :type column: int
        :rtype: float
        """
        lastdp = [[0]*n for _ in range(n)]
        di = [-2, -1, 1, 2, 2, 1, -1, -2]
        dj = [-1, -2, -2, -1, 1, 2, 2, 1]
        lastdp[row][column] = 1
        
        for _ in range(k):
            dp = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for t in range(8):
                        x, y = i + di[t], j + dj[t]
                        if x >= 0 and x < n and y >= 0 and y < n:
                            dp[i][j] += lastdp[x][y]/8.0
            lastdp = dp
            
        res = 0
        for i in range(n):
            for j in range(n):
                res += lastdp[i][j]
        return res