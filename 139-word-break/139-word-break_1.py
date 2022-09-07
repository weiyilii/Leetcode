class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DP
        l = len(s)
        dp = [False]*l
        for i in range(l):
            for word in wordDict:
                wlen = len(word)
                if s[i - wlen + 1:i + 1] == word and (dp[i - wlen] or i - wlen == -1):
                    dp[i] = True
        return dp[-1]
