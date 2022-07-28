class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(left, right):
            if left == right:
                return left
            mid = left + (right - left)//2
            if mid + 1 <= right and nums[mid] < nums[mid + 1]:
                return dfs(mid + 1, right)
            elif mid - 1 >= left and nums[mid] < nums[mid - 1]:
                return dfs(left, mid)
            else:
                return mid
        res = dfs(0, len(nums) - 1)
        return res
            