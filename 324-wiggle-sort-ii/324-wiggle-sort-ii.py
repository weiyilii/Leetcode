class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        copy = sorted(nums, reverse = True)
        n = len(nums)
        m = n//2
        
        for i in range(m):
            j = i*2 + 1
            nums[j] = copy[i]
        for i in range(m, n):
            j = (i-m)*2
            nums[j] = copy[i]