class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """        
        def helper(nums, sort, a, b):
            if a >= b:
                return
            
            mid = a + (b - a) // 2
            
            helper(nums, sort, a, mid)
            helper(nums, sort, mid+1, b)
            
            for i in range(a, mid+1):
                #print(nums[i], sort[mid+1:b+1])
                low, high = mid+1, b
                while low <= high:
                    middle = low + (high - low) // 2
                    if nums[i] > sort[middle]:
                        low = middle + 1
                    else:
                        high = middle - 1
                count[i] += low - mid - 1
                #print(nums[i], sort[mid+1:b+1], mid, high, count)
            
            sort[a:b+1] = sorted(sort[a:b+1])
            
        n = len(nums)
        count = [0]*n
        sort = nums[:]
        helper(nums, sort, 0, n-1)
        return count
                