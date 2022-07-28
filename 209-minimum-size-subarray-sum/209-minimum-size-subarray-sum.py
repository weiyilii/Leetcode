class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, nsum = 0, 0
        res = float('inf')
        for i in range(len(nums)):
            nsum += nums[i]
            while nsum >= target:
                res = min(res, i - left + 1)
                nsum -= nums[left]
                left += 1
        return res if res <= len(nums) else 0