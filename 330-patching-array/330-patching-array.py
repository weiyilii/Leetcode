class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i, add, miss = 0, 0, 1
        l = len(nums)
        
        while miss <= n:
            if i < l and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                add += 1
                
        return add