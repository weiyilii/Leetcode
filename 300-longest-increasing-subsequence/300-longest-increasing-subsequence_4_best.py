class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP & Binary search
        n = len(nums)
        tail = []
        size = 0
        for num in nums:
            if not tail or num > tail[-1]:
                tail.append(num)
                size += 1
            else:
                l, r = 0, size
                while l < r:
                    m = l + (r - l) // 2
                    if tail[m] < num:
                        l = m + 1
                    else:
                        r = m
                tail[l] = num
        return size
