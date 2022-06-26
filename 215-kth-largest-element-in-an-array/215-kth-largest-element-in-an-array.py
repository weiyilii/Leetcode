class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from heapq import *
        heapify(nums)
        l = len(nums)
        for i in range(l-k):
            heappop(nums)
        return heappop(nums)