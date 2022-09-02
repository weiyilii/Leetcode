class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        l = self.gcd(len(str1), len(str2))
        return str1[:l]
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)