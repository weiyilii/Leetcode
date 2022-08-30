class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        l = len(palindrome)
        
        if l <= 1:
            return ""
        
        for i in range(l//2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
        
        return palindrome[:-1] + "b"