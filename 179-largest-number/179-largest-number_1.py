class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Intuition: sort str(num) descendingly in lexicographical order: "98" > "7654"
        # However, there might be a problem
        # if 2 strs have same prefix like: "51" and "5"
        # Lexicographically, "51" > "5"
        # but "551" > "515"
        # In this case, we just need to replicate str for enough times
        # for example, longest str has a length of 5
        # replicate "551" by (5//3 + 1 = 2) times -> "551551"
        # replicate "5" by (5//1 + 1 = 6) times -> "555555"
        # now compare them "555555" > "551551"
        # just sort them in lecograohical order them concatenate all
        
        nums = map(str, nums)
        longest = max([len(num) for num in nums])
        sort_key = lambda x: x*(longest//len(x) + 1)
        nums = sorted(nums, key = sort_key, reverse = True)
        nums = ''.join(nums)
        return '0' if nums[0] == '0' else nums
