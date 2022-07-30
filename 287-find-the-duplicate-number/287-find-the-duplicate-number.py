class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left