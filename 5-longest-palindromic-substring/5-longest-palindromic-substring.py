class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxl = 1
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            l = max(len1, len2)
            if l > maxl:
                maxl = l
                start = i - (l-1)//2
                end = i + l//2
        return s[start:end+1]
    
    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j - i - 1