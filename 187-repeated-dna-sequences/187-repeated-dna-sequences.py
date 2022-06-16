class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        counts = collections.defaultdict(int)
        for i in range(len(s)-9):
            counts[s[i:i+10]] += 1
        res = [key for key, value in counts.items() if value > 1]
        return res