class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        
        l = len(s)
        dp = [0]*(l + 1)
        dp[0] = 1
        if s[0] != "0":
            dp[1] = 1
        for i in range(1, l):
            num = int(s[i-1:i+1])
            if s[i] == "0":
                if num > 0 and num <= 26:
                    dp[i+1] += dp[i-1]
            else:
                dp[i+1] += dp[i]
                if num >= 10 and num <= 26:
                    dp[i+1] += dp[i-1]
        return dp[-1]