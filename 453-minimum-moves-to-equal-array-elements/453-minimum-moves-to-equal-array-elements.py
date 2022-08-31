class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # After sorting, nums[0] is min, nums[-1] is max, increment all except nums[-1] by their difference
        # then min is still nums[0], max becomes nums[-2], do the same increment
        # until min == max
        nums.sort()
        pos = len(nums) - 1
        res = 0
        while nums[0] < nums[pos]:
            res += nums[pos] - nums[0]
            pos -= 1
        return res
