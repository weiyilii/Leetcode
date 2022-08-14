class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        for u in graph:
            graph[u].sort(key = lambda x: x[0])
        visited = {} 
        
        def dfs(src, dst, time):
            if dst not in visited or time < visited[dst]:
                visited[dst] = time
                if dst in graph:
                    for w, v in graph[dst]:
                        dfs(dst, v, time + w)
        
        dfs(k, k, 0)
        if len(visited) < n:
            return -1
        return max(visited.values())