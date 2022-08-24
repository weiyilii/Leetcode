class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        res = dp[0]
        
        for i in range(1, len(nums)):
            if dp[i-1] >= 0:
                dp[i] = nums[i] + dp[i-1]
            else:
                dp[i] = nums[i]
            res = max(res, dp[i])
        
        return res