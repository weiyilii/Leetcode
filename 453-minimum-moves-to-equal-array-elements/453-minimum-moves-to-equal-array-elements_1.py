class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Math, incrment n-1 elements by one is equal to decrement one element
        # Only need to decrement each element to min
        min_val = min(nums)
        return sum(nums) - min_val*len(nums)
