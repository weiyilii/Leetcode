class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = lambda x: len(x))
        n = len(words)
        dp = {}
        res = 1
        for w in words:
            seqlen = 0
            for i in range(len(w)):
                new = w[:i] + w[i+1:]
                if new in dp:
                    seqlen = max(seqlen, dp[new])
            dp[w] = seqlen + 1
            res = max(res, dp[w])
        return res