class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Heap
        # Find the kth smallest from n sorted arrays
        from heapq import heappush, heappop
        n = len(matrix)
        h = []
        # Initiate the min heap with all the first element in each row
        for i in range(n):
            heappush(h, (matrix[i][0], (i, 0)))
        while k > 0:
            (res, (i, j)) = heappop(h)
            # everytime pop an element, push the right element in the same row into heap if not out of list range
            if j < n-1:
                heappush(h, (matrix[i][j+1], (i, j+1)))
            k -= 1
        return res
