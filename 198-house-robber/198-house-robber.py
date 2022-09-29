class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        
        dp = [0]*(l+1)
        dp[0], dp[1] = 0, nums[0]
        
        for i in range(2, l+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        
        return dp[-1]