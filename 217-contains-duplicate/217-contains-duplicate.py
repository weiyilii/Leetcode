class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsset = set(nums)
        if len(nums) > len(numsset):
            return True
        return False