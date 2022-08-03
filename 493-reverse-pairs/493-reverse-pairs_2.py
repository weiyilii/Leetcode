class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def helper(nums, left, right):
            if left >= right:
                return 0
            
            mid = left + (right - left) // 2
            count = helper(nums, left, mid) + helper(nums, mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):        
                while j <= right and nums[i] > 2*nums[j]:
                    j += 1
                count += j - mid - 1
                
            # Equivalent to solution 1 merge
            nums[left:right+1] = sorted(nums[left:right+1])
                    
            return count
        
        return helper(nums, 0, len(nums) - 1)
                
