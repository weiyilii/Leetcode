class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        m, n = len(key), len(ring)
        dp = [[float('inf') for j in range(n)] for i in range(m)]
        pos = dict()
        for i, r in enumerate(ring):
            if r in pos:
                pos[r].append(i)
            else:
                pos[r] = [i]
                    
        for j in pos[key[0]]:
            dp[0][j] = min(dp[0][j], j, n-j)
            
        for i in range(1, m):
            for j in pos[key[i]]:
                for k in pos[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + abs(j-k), dp[i-1][k] + n-abs(j-k))
        
        res = float('inf')
        for j in range(n):
            res = min(res, dp[m-1][j])
        return res + m