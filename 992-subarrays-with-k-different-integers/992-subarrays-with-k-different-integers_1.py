class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # number of subarrays having exactly k numbers = subarrays having at most k numbers - subarrays having at most k-1 numbers
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    
    def atMost(self, nums, k):
        i, res = 0, 0
        counter = collections.defaultdict(int)
        for j in range(len(nums)):
            if counter[nums[j]] == 0:
                # if nums[j] not in counter, that means subarray not having nums[j], we used a place for different number, k -= 1
                k -= 1
            counter[nums[j]] += 1
            while k < 0:
                # k = 0 means subarray used exactly all the places for different numbers
                # k < 0 means subarray having  more than original k unique numbers
                # increment i to remove nums[i] from subarray
                counter[nums[i]] -= 1
                if counter[nums[i]] == 0:
                    k += 1
                i += 1
            # subarrays within nums from i to j-1 have been included, only increment new subarrays having nums[j]
            res += j - i + 1
        return res
