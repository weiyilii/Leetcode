class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev, cur = [1], [1]
        for i in range(1, rowIndex+1):
            cur = [1]
            for j in range(i-1):
                cur.append(prev[j] + prev[j+1])
            cur.append(1)
            prev = cur
        return cur
        