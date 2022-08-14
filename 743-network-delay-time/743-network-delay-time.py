class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from heapq import heappush, heappop
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        h = []
        visited = {}
        heappush(h, (0, k))
        while h:
            t, node = heappop(h)
            if node not in visited or t < visited[node]:
                visited[node] = t
                for w, v in graph[node]:
                    heappush(h, (w+t, v))
        return -1 if len(visited) < n else max(visited.values())