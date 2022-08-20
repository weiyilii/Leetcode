class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Iterative, DP idea
        # Use previous subsets. Add new elements to each previous subset and form a new subset
        # cur stores last added items
        res, cur = [[]], []
        nums.sort()
        
        for i in range(len(nums)):
            # if nums[i] == nums[i-1], only append nums[i] to subsets whose last item is nums[i-1] which are in cur
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            # if nums[i] != nums[i-1], append nums[i] to all previous subsets
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        
        return res
