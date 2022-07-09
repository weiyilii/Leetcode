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