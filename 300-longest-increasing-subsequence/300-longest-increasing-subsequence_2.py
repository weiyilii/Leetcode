class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        # Front to end
        n = len(nums)
        lis = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)
