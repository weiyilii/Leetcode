class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return 0
        
        dp = [10001]*l
        dp[-1] = 0
        
        for i in range(l-2, -1, -1):
            for j in range(1, nums[i]+1):
                if i + j <= l-1:
                    dp[i] = min(dp[i], dp[i+j] + 1)
        return dp[0]