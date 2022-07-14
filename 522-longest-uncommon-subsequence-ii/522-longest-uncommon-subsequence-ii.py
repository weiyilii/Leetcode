class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def ifSub(w1, w2):
            n1, n2 = len(w1), len(w2)
            i, j = 0, 0
            while i < n1 and j < n2:
                if w1[i] == w2[j]:
                    i += 1
                j += 1
            return i == n1
        
        strs.sort(key = len, reverse = True)
        for i in range(len(strs)):
            res = False
            for j in range(len(strs)):
                if i != j:
                    res = (res or ifSub(strs[i], strs[j]))
            if not res:
                return len(strs[i])
        return -1