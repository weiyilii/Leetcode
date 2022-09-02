class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left)//2
            kmax = ksum = sum(nums[:mid])
            
            for i in range(len(nums) - mid):
                ksum += nums[i+mid] - nums[i]
                kmax = max(kmax, ksum)
            
            if kmax == target:
                return mid
            elif kmax < target:
                left = mid + 1
            else:
                right = mid
        return right