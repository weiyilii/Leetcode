class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        tail = [0]*n
        size = 0
        for num in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if num > tail[m]:
                    i = m + 1
                else:
                    j = m
            tail[i] = num
            size = max(size, i + 1)
        return size