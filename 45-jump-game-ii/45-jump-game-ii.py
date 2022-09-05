class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, currend, far = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == currend:
                jumps += 1
                currend = far
        return jumps