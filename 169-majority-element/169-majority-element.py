class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate, count = nums[i], 1
            else:
                count += 1 if candidate == nums[i] else -1
        return candidate