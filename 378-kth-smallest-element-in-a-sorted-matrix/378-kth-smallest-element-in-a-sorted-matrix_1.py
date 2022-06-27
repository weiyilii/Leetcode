class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Heap, similar to 373
        from heapq import heappush, heappop
        h = [(matrix[0][0], (0, 0))]
        visited = {(0, 0)}
        n = len(matrix)
        while k > 0:
            (res, (i, j)) = heappop(h)
            new_i = i+1 if i < n-1 else i
            new_j = j+1 if j < n-1 else j
            if (new_i, j) not in visited:
                heappush(h, (matrix[new_i][j], (new_i, j)))
                visited.add((new_i, j))
            if (i, new_j) not in visited:
                heappush(h, (matrix[i][new_j], (i, new_j)))
                visited.add((i, new_j))
            k -= 1
        return res
