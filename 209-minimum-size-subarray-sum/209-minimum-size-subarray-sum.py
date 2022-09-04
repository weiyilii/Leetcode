class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, ksum = 0, 0
        res = float('inf')
        for i in range(len(nums)):
            ksum += nums[i]
            while ksum >= target:
                res = min(res, i - left + 1)
                ksum -= nums[left]
                left += 1
        if res > len(nums):
            return 0
        else:
            return res