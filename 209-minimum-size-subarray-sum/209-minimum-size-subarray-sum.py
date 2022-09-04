class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < target:
            return 0
        
        left, right = 1, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            ksum = kmax = sum(nums[:mid])
            for i in range(len(nums) - mid):
                ksum += nums[i + mid] - nums[i]
                kmax = max(ksum, kmax)
            
            if kmax == target:
                return mid
            elif kmax > target:
                right = mid
            else:
                left = mid + 1
        return right