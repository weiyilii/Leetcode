class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        sequence, repeated = set(), set()
        
        for i in range(len(s) - 9):
            sub = s[i: i+10]
            if sub in sequence:
                repeated.add(sub)
            sequence.add(sub)
            
        return list(repeated)