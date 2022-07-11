class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp = []
        res = []
        nums.sort()
        for num in nums:
            dp.append([num])
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
            if len(dp[i]) > len(res):
                res = dp[i]
        return res