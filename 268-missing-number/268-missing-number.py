class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use index as hash, walk through nums
        # for each num, modify nums[num]
        # walk through again if num > 0, that means its index has not been visited
        # index as a number is not in nums
        # be careful about index=n and 0
        # after modification, if no negative number
        # that means index of 0 is missed in nums
        nums.append(1)
        
        for num in nums[:len(nums)-1]:
            nums[abs(num)] *= (-1)
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        
        return nums.index(0)