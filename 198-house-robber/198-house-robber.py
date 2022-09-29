class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        
        dp = [0]*l
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(1, l):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]