class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Negative marking (hashmap idea)
        # Still modifies the array
        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                return cur
            nums[cur] = -nums[cur]
