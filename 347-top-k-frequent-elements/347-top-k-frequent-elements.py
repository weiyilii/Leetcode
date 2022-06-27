class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from heapq import heappush, heappop
        counts = collections.Counter(nums)
        h, res = [], []
        for num, count in counts.items():
            heappush(h, (-count, num))
        for i in range(k):
            res.append(heappop(h)[1])
        return res