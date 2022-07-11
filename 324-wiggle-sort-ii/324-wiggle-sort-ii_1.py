class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # sort the array descendingly
        # find mid and divide into left and right (mid is in right)
        # left elements (large) go to index = 1, 3, 5, 7 ...
        # right elements (small) go to index = 0, 2, 4, 6 ...
        
        copy = sorted(nums, reverse = True)
        n = len(nums)
        m = n//2
        
        for i in range(m):
            j = i*2 + 1
            nums[j] = copy[i]
        for i in range(m, n):
            j = (i-m)*2
            nums[j] = copy[i]
