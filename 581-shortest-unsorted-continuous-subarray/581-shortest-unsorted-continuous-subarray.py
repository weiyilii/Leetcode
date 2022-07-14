class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = n, 0
        
        max_seen = float("-inf")
        for i in range(n):
            if nums[i] < max_seen:
                right = i
            max_seen = max(nums[i], max_seen)
        
        min_seen = float("inf")
        for i in range(n)[::-1]:
            if nums[i] > min_seen:
                left = i
            min_seen = min(nums[i], min_seen)
        
        return right-left+1 if left < right else 0