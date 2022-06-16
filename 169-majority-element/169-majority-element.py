class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        # Counting majority element as +1 and others as -1
        # change candidate of majority to current element when count == 0
        candidate, count = nums[0], 1
        for i in range(1, len(nums)):
            if count == 0:
                candidate, count = nums[i], 1
            else:
                count += (1 if candidate == nums[i] else -1)
        return candidate