class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = " " + s
        p = " " + p
        m, n = len(s), len(p)
        dp = [[False]*n for _ in range(m)]
        dp[0][0] = True
        for i in range(1, m):
            dp[i][0] = False
        j = 1
        while j < n and p[j] == "*":
            dp[0][j] = True
            j += 1
        
        for i in range(1, m):
            for j in range(1, n):
                if s[i] == p[j] or p[j] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = (dp[i-1][j] or dp[i][j-1])
                    
        return dp[-1][-1]