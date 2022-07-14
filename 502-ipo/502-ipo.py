class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        from heapq import heappush, heappop
        h = []
        i = 0
        projects = sorted(zip(profits, capital), key = lambda x: x[1])
        for _ in range(k):
            while i < len(projects) and w >= projects[i][1]:
                heappush(h, -projects[i][0])
                i += 1
            if h:
                w -= heappop(h)
        return w