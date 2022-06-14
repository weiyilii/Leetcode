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
                # res[i] is true when: 
                # 1. w matches sub str ending at ith element of res
                # 2. res is true at the left of that sub str or it's 1st word
                if w == s[i-w_len+1 : i+1] and (res[i-w_len] or i-w_len == -1):
                    res[i] = True
        return res[-1]