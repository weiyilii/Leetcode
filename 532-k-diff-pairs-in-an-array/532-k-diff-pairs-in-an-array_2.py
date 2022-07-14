class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Hashmap
        
        count = collections.Counter(nums)
        res = 0
        for key in count:
            if (k > 0 and key + k in count) or (k == 0 and count[key] > 1):
                res += 1
        return res
