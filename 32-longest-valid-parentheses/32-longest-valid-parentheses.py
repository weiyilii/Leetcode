class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        dp = [0]*(len(s))
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i >= 2 else 2
                else:
                    if i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
                        dp[i] = dp[i-1] + 2
                        if i - dp[i-1] - 2 >= 0:
                            dp[i] += dp[i - dp[i-1] - 2]
            res = max(res, dp[i])
        return res