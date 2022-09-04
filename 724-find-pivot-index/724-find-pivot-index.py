class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        left, right = [0]*l, [0]*l
        left[0], right[-1] = 0, 0
        for i in range(1, l):
            left[i] = nums[i-1] + left[i-1]
        for i in range(l-2, -1, -1):
            right[i] = nums[i+1] + right[i+1]
        for i in range(l):
            if left[i] == right[i]:
                return i
        return -1