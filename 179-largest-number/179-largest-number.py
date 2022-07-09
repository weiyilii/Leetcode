class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        longest = max([len(num) for num in nums])
        sort_key = lambda x: x*(longest//len(x) + 1)
        nums = sorted(nums, key = sort_key, reverse = True)
        nums = ''.join(nums)
        return '0' if nums[0] == '0' else nums