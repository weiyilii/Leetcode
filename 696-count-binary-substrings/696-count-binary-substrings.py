class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        prev, count = 0, 1
        i = 1
        while i < len(s):
            if s[i] == s[i-1]:
                count += 1
            else:
                res += min(prev, count)
                prev = count
                count = 1
            i += 1
        res += min(prev, count)
        return res