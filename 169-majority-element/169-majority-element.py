class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        d = collections.Counter(nums)
        for num in d:
            if d[num] > (n//2):
                return num