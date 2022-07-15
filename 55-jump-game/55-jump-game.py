class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_seen = 0
        for i in range(n-1):
            if i <= max_seen:
                max_seen = max(max_seen, i+nums[i])
        return max_seen >= n-1