class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                return cur
            nums[cur] = -nums[cur]