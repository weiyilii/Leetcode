class Solution(object):
    # given nums, select l elements as largest array while preserving order
    def maxSingle(self, nums, l):
        stack = []
        n = len(nums)
        for i in range(n):
            while stack and nums[i] > stack[-1] and n-i+len(stack) > l:
                stack.pop()
            if len(stack) < l:
                stack.append(nums[i])  
        return stack
    # given nums1 and nums2, merge them into one largest array
    def mergeMax(self, n1, n2):
        res = []
        while n1 or n2:
            if n1 > n2:
                res.append(n1[0])
                n1 = n1[1:]
            else:
                res.append(n2[0])
                n2 = n2[1:]
        return res
    
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        res = [0]*k
        # k elements in total, try select (0, k), (1, k-1), (2, k-2).... elements
        # from nums1 and nums2 as two arrays respectively
        # merge them 2 into 1 as current max array
        # comapre all possible max arrays
        for i in range(k+1):
            j = k-i
            if i > m or j > n:
                continue
            n1 = self.maxSingle(nums1, i)
            n2 = self.maxSingle(nums2, j)
            res = max(res, self.mergeMax(n1, n2))
        return res