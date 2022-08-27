class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(i-1):
                row.append(res[-1][j] + res[-1][j+1])
            row.append(1)
            res.append(row)
        return res