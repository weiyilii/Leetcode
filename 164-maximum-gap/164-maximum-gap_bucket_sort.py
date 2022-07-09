class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low,  high = min(nums), max(nums)
        n = len(nums)
        
        if n <= 2 or low == high:
            return high-low
        
        # n = len(nums)
        # divide elements into n-1 buckets
        # n elements have n-1 gaps
        # if we have n-1 buckets, one bucket will have 2 elements, others have only 1
        # for the bucket having 2 elements: the gap between them 2 must be <= (high-low)/(n-1) (bucket's possible range)
        # across all n-1 buckets, there are n-2 gaps between every 2 consecutive buckets
        # there must be one gap >= (high-low)//(n-1)
        # otherwise, the total gap would be < (n-2)*(high-low)/(n-1) + (high-low)/(n-1) = (n-1)*(high-low)/(n-1) = high-low
        # conflicts with the question
        # so just compare gaps between (first bucket's max and second bucket's min; second bucket's max and third bucket's min .....)
        
        buckets = collections.defaultdict(list)
        for num in nums:
            if num == high:
                buckets[n-2].append(num)
            else:
                key = (n-1)*(num-low)//(high-low)
                buckets[key].append(num)
        diff = []
        for bucket in buckets.values():
            if bucket:
                diff.append([min(bucket), max(bucket)])
        res = 0
        for i in range(1, len(diff)):
            res = max(res, diff[i][0]-diff[i-1][1])
        return res
