class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Divide and Conquer
        # array, index from left to right with mid
        # max subarray possibilities:
        # 1. entirely within left half: left, mid-1 (recursively call)
        # 2. entirely within right half: mid+1, right (recursively call)
        # 3. having mid inside: [somewhere:mid] + [mid] + [mid+1:somewhere] (loop sum and compare) (must include mid and may extend both sides)
        # then compare 3 options, return the max (combine)
        def dq(left, right):
            if left > right:
                return float('-inf')
            mid = left + (right - left) // 2
            left_sum, right_sum = 0, 0
            cur_sum = 0
            for i in range(mid-1, left-1, -1):
                cur_sum += nums[i]
                left_sum = max(left_sum, cur_sum)
            cur_sum = 0
            for i in range(mid+1, right+1):
                cur_sum += nums[i]
                right_sum = max(right_sum, cur_sum)
            return max(dq(left, mid-1), dq(mid+1, right), nums[mid] + left_sum + right_sum)
        
        return dq(0, len(nums)-1)
