class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        from heapq import heappush, heappop, heapify
        res = 0
        heapify(sticks)
        while len(sticks) > 1:
            l1 = heappop(sticks)
            l2 = heappop(sticks)
            res += l1 + l2
            heappush(sticks, l1 + l2)
        return res