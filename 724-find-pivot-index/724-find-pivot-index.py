class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        left = 0
        s = sum(nums)
        for i in range(l):
            if left == s - left - nums[i]:
                return i
            left += nums[i]
        return -1