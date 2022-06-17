class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count1 = collections.Counter(s)
        count2 = collections.Counter(t)
        
        return count1 == count2