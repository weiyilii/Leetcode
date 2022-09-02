class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return 0
        
        nums.sort()
        res = 0
        for i in range(l - 2):
            res += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return res
    
    def twoSumSmaller(self, nums, i, target):
        l = len(nums)
        if i > l - 2:
            return 0
        left, right = i, l - 1
        res = 0
        while left < right:
            if nums[left] + nums[right] >= target:
                right -= 1
            else:
                res += right - left
                left += 1
        return res