class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0 
        # time complexity = O(1) using set
        nums_set = set(nums)
        for num in nums_set:
            # start sequence from num when num-1 not in set
            if num - 1 not in nums_set:
                cur_len = 1
                cur_num = num
                # expand sequence
                while cur_num + 1 in nums_set:
                    cur_len += 1
                    cur_num += 1
                max_len = max(cur_len, max_len)
        return max_len