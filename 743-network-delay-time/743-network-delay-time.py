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
            graph[u].append((v, w))
            
        visited = {} 
        
        def dfs(src, dst, time):
            if dst not in visited or time < visited[dst]:
                visited[dst] = time
                if dst in graph:
                    for v, w in graph[dst]:
                        dfs(dst, v, time + w)
        
        dfs(k, k, 0)
        if len(visited) < n:
            return -1
        return max(visited.values())