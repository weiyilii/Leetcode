class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Divide nums into buckets each bucket can contain numbers with a range of t (like: 0, 1, 2, ..., t) (t+1 elements)
        # (1) Once a bucket has more than 1 element, that means 2 elements within the range t, they satisfy conditions, return True
        # (2) Other circumstances: elements within range t are in neighboring buckets
        
        # b as a dictionary holding buckets
        b = {}
        for i in range(len(nums)):
            num = nums[i]
            # m is the key of the bucket
            m = num // (t+1)
            
            # (1) if m is already in b: 2 elements will be in the same bucket
            if m in b:
                return True
            # (2) previous bucket has an element satisfying abs(nums[i] - nums[j]) <= t
            elif m-1 in b and num - b[m-1] <= t:
                return True
            # (2) next bucket has an element satisfying abs(nums[i] - nums[j]) <= t
            elif m+1 in b and b[m+1] - num <= t:
                return True
            # record this element in its bucket
            b[m] = nums[i]
            # sliding window size is k, if i exceeds k, evrytime delete the bucket holding the expired element
            if i >= k:
                del b[nums[i-k]//(t+1)]
        return False
