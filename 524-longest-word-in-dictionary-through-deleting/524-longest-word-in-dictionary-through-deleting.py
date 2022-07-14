class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        def isSub(w1, w2):
            n1, n2 = len(w1), len(w2)
            i, j = 0, 0
            while i < n1 and j < n2:
                if w1[i] == w2[j]:
                    i += 1
                j += 1
            return i == n1
            
        dictionary.sort(key = lambda x: (-len(x), x))
        for d in dictionary:
            if isSub(d, s):
                return d
        return ''