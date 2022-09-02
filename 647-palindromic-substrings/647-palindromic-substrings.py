class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for distance in range(1, l):
            for i in range(l - distance):
                j = i + distance
                dp[i][j] += dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                if s[i] == s[j] and s[i+1:j] == s[i+1:j][::-1]:
                    dp[i][j] += 1
        return dp[0][-1]