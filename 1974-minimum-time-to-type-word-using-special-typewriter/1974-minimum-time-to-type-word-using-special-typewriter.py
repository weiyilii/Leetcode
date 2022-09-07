class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        src = 0
        res = 0
        for c in word:
            dst = ord(c) - ord("a")
            res += min(abs(dst - src), min(dst, src) + 26 - max(dst, src))
            src = dst
        return res + len(word)