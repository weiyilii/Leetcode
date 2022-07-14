class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        res = 0
        for key in count:
            if key + 1 in count:
                res = max(res, count[key] + count[key+1])
        return res