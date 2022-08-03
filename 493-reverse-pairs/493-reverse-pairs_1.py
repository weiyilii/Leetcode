class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Divide and conquer, merge sort
        def helper(nums, left, right):
            if left >= right:
                return 0
            
            mid = left + (right - left) // 2
            count = helper(nums, left, mid) + helper(nums, mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                # Important! No need to initialize j every time, it can inherit from last time as nums left and right half are sorted
                while j <= right and nums[i] > 2*nums[j]:
                    j += 1
                count += j - mid - 1
                
            tmp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    tmp.append(nums[j])
                    j += 1
            if i <= mid:
                tmp += nums[i:mid+1]
            else:
                tmp += nums[j:right+1]
            
            nums[left:right+1] = tmp
                    
            return count
        
        return helper(nums, 0, len(nums) - 1)
                
