class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        n = len(matrix)
        h = []
        for i in range(n):
            heappush(h, (matrix[i][0], (i, 0)))
        while k > 0:
            (res, (i, j)) = heappop(h)
            if j < n-1:
                heappush(h, (matrix[i][j+1], (i, j+1)))
            k -= 1
        return res