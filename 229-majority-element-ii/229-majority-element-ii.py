class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = collections.Counter(nums)
        for num in dic:
            if dic[num] > len(nums) // 3:
                res.append(num)
        return res