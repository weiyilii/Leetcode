class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)
        
        for num in nums[:len(nums)-1]:
            nums[abs(num)] *= (-1)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        
        return nums.index(0)