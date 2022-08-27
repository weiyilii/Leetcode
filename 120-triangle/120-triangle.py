class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        for i in range(1, m):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == i:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])