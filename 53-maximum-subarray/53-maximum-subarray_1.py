class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        prev = nums[0]
        res = prev
        for i in range(1, len(nums)):
            if prev >= 0:
                cur = nums[i] + prev
            else:
                cur = nums[i]
            prev = cur
            res = max(res, cur)
        return res
