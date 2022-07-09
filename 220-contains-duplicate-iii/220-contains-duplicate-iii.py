class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        b = {}
        for i in range(len(nums)):
            num = nums[i]
            m = num // (t+1)
            if m in b:
                return True
            elif m-1 in b and num - b[m-1] <= t:
                return True
            elif m+1 in b and b[m+1] - num <= t:
                return True
            b[m] = nums[i]
            if i >= k:
                del b[nums[i-k]//(t+1)]
        return False