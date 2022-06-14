class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [False]*(len(s))
        for i in range(len(s)):
            for w in wordDict:
                w_len = len(w)
                if w == s[i-w_len+1 : i+1] and (res[i-w_len] or i-w_len == -1):
                    res[i] = True
        return res[-1]