class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[j] += 1
                else:
                    dp[j] = 0
            res = max(res, self.hist(dp))
        return res
        
    def hist(self, heights):
        res = 0
        stack = [-1]
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h*w)
            stack.append(i)
        return res
        