class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # dp[i]: number of steps needed to jump from i to last index
        # dp[-1] = 0: already at last index, no need to jump
        # iterate from back to forth
        l = len(nums)
        if l <= 1:
            return 0
        
        dp = [10001]*l
        dp[-1] = 0
        
        for i in range(l-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j <= l-1:
                    # j is step length
                    # i + j is the index that may reach
                    # dp[i+j] + 1 means jump from i to i+j needs one step, and from i + j to last index need dp[i+j] steps
                    dp[i] = min(dp[i], dp[i+j] + 1)
        return dp[0]
