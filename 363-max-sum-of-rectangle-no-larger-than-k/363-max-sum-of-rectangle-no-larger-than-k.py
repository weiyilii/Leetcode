from sortedcontainers import SortedList
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for r1 in range(m):
            array = [0]*n
            for r2 in range(r1, m):
                for c in range(n):
                    array[c] += matrix[r2][c]
                res = max(res, self.maxSumSubarray(array, k))
        return res        
    
    def maxSumSubarray(self, array, k):
        ans = float('-inf')
        n = len(array)
        presum = SortedList([0])
        right = 0
        for i in range(n):
            right += array[i]
            left = self.findLeft(presum, right - k)
            if left != None:
                ans = max(ans, right - left)
            presum.add(right)
        return ans
    
    def findLeft(self, array, key):
        idx = array.bisect_left(key)
        if idx < len(array) and idx >= 0:
            return array[idx]
        return None