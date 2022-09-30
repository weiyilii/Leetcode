class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        
        def expand(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return (i+1, j-1)
        
        for i in range(len(s)):
            res = expand(i, i)
            if res[1] - res[0] > right - left:
                left, right = res[0], res[1]
        
        for i in range(len(s)-1):
            res = expand(i, i+1)
            if res[1] - res[0] > right - left:
                left, right = res[0], res[1]
        
        return s[left:right+1]