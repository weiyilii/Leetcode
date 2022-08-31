class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        pos = len(nums) - 1
        res = 0
        while nums[0] < nums[pos]:
            res += nums[pos] - nums[0]
            pos -= 1
        return res