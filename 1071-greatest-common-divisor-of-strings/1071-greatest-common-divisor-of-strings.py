class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        res = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return res
            d = str1[:i+1]
            if len(str1) == str1.count(d)*(i+1) and len(str2) == str2.count(d)*(i+1):
                res = d
        return res