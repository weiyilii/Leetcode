class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)
            
        left, right = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)
            if r1 - l1 < r2 - l2:
                l1, r1 = l2, r2
            if r1 - l1 > right - left:
                left, right = l1, r1
        return s[left:right+1]