class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        
        match1, match2 = {}, {}
        for i in range(len(s)):
            char = pattern[i]
            word = s[i]
            if char in match1:
                if match1[char] != word:
                    return False
            else:
                match1[char] = word
                
            if word in match2:
                if match2[word] != char:
                    return False
            else:
                match2[word] = char
        
        return True