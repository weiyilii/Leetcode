class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    
    def atMost(self, nums, k):
        i, res = 0, 0
        counter = collections.defaultdict(int)
        for j in range(len(nums)):
            if counter[nums[j]] == 0:
                k -= 1
            counter[nums[j]] += 1
            while k < 0:
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    k += 1
                i += 1
            res += j - i + 1
        return res