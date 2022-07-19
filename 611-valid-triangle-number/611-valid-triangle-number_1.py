class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        # i < j < k, nums[i] < nums[j] < nums[k]
        # just make sure nums[i] + nums[j] > nums[k], then it is a valid triangle
        # iterate k from 2 to len-1
        # start with i = 0, j = k-1
        # if it is valid then all j-i pairs are valid: update res and j = j-1
        # else: update i = i+1
        for k in range(2, len(nums)):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j-i
                    j -= 1
                else:
                    i += 1
        return res
