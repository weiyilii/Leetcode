class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        i, j = 0, len(nums)-1
        
        while i <= j:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        
        return res