class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k
        
        def quickSelect(left, right):
            pivot = nums[right]
            p = left
            # after the whole process,  p means elements from left to p are <= pivot
            # iterate from left to right-1
            # everytime meets an element <= pivot
            # swap it with nums[p]
            # summary: select elements from left to right-1 which are less than pivot
            # put them in the front of nums
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[right] = nums[right], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p+1, right)
            else:
                return quickSelect(left, p-1)
        
        return quickSelect(0, len(nums)-1)
