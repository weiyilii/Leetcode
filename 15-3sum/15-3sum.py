class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        if l < 3:
            return 0
        res = []
        nums.sort()
        i = 0
        while i < l - 2:
            if i == 0 or nums[i] != nums[i-1]:
                res += self.twoSum(nums, i + 1, -nums[i])
            i += 1
        return res
    
    def twoSum(self, nums, i, target):
        l = len(nums)
        if i > l - 2:
            return 0
        res = []
        left, right = i, l - 1
        prev = nums[right] + 1
        while left < right:
            if nums[right] != prev and nums[left] + nums[right] == target:
                res.append([nums[i - 1], nums[left], nums[right]])
                prev = nums[right]
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return res