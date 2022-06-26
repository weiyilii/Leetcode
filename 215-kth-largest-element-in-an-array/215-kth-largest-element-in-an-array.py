class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Heap
        # Default: min heap
        # kth largest = [len(nums)-k+1]th smallest
        from heapq import *
        heapify(nums)
        l = len(nums)
        for i in range(l-k):
            heappop(nums)
        return heappop(nums)