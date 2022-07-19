class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        mid = False
        res = 0
        for key in dic:
            if dic[key] % 2 == 0:
                res += dic[key]
            else:
                res += dic[key] - 1
                mid = True
        return res+1 if mid else res