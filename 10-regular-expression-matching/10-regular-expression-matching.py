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
        dp = [[False]*(n) for _ in range(m)]
        
        dp[0][0] = True
        for j in range(1, n):
            if p[j] == "*":
                dp[0][j] = dp[0][j-2]
            
        for i in range(1, m):
            for j in range(1, n):
                if p[j] == "." or s[i] == p[j]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j-2] or ((s[i] == p[j-1] or p[j-1] == ".") and dp[i-1][j])
        
        return dp[-1][-1]