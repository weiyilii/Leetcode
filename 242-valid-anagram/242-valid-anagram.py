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
        
        for key in count1:
            if count1[key] != count2[key]:
                return False
        
        return True