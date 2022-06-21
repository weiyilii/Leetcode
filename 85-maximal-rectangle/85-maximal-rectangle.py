class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        height = [0]*(n+1)
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # for each row, create a histogram, then apply #84
            stack = [-1]
            for j in range(n+1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - stack[-1] -1
                    res = max(res, h*w)
                stack.append(j)
        return res