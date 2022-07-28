class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search
        
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            
            max_k = sum_k = sum(nums[:mid])
            for i in range(1, n - mid + 1):
                # Important! Sum of sliding window
                sum_k = sum_k-nums[i-1]+nums[i+mid-1]
                max_k = max(max_k, sum_k)
                
            if max_k == target:
                return mid
            elif max_k < target:
                left = mid + 1
            else:
                right = mid
        return right
