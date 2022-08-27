class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(t), len(s)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if s[0] == t[0]:
            dp[0][0] = 1
        for j in range(1, n):
            dp[0][j] += dp[0][j-1]
            if s[j] == t[0]:
                dp[0][j] += 1
        
        for i in range(1, m):
            for j in range(1, n):
                if t[i] == s[j]:
                    dp[i][j] += dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]