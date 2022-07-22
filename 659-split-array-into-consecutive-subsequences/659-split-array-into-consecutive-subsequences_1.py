class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Greedy, map
        # use 2 maps: nums frequency, subsequences (last element as key, count of subsequences ending with this element as value)
        # check if current num can be appended to an exsiting subsequence or form a new one with num+1 and num+2
        
        freq = collections.Counter(nums)
        subs = collections.defaultdict(int)
        
        for num in nums:
            if freq[num] == 0:
                continue
            elif subs[num-1] > 0:
                subs[num-1] -= 1
                subs[num] += 1
                freq[num] -= 1
            elif subs[num-1] == 0 and num+1 in freq and num+2 in freq and freq[num+1] > 0 and freq[num+2] > 0:
                subs[num+2] += 1
                freq[num] -= 1
                freq[num+1] -= 1
                freq[num+2] -= 1
            else:
                return False
        
        return True
                
