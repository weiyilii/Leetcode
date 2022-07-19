class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # Binary Search
        # result must be within [max element, sum of elements] (of the array)
        # doing a binary search in this range
        # each value will be the possible result
        # determine if this value satisfies the requirement (m)
        
        sums = sum(nums)
        max_element = max(nums)
        
        left, right = max_element, sums
        
        while left < right:
            mid = left + (right - left) // 2
            splits = 0
            sum_sub = 0
            for num in nums:
                if sum_sub + num <= mid:
                    sum_sub += num
                else:
                    sum_sub = num
                    splits += 1
            if splits + 1 <= m:
                right = mid
            else:
                left = mid + 1
                
        return left
