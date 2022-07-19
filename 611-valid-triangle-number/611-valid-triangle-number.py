class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for k in range(2, len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j-i
                    j -= 1
                else:
                    i += 1
        return res