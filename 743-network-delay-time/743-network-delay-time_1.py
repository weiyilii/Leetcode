class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        # BFS
        # Layer by layer, accumulate time
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        visited = {}
        q = collections.deque()
        q.append((k, 0))
        while q:
            node, t = q.popleft()
            if node not in visited or t < visited[node]:
                visited[node] = t
                # Only when the condition above satisfied, append its children to queue, otherwise will get duplicates
                for child, time in graph[node]:
                    q.append((child, t + time))
        if len(visited) < n:
            return -1
        return max(visited.values())
