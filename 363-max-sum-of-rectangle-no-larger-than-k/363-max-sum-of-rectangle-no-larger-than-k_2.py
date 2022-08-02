from sortedcontainers import SortedList
class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # TLE
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
        if array[-1] < key:
            return None
        low, high = 0, len(array) - 1
        while low < high:
            mid = low + (high - low) // 2
            if array[mid] == key:
                return array[mid]
            elif array[mid] < key:
                low = mid + 1
            else:
                high = mid
        return array[high]
