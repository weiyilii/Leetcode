class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque
        
        graph = {}
        n = len(colors)
        degree = [0]*n
        
        for src, dst in edges:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
            degree[dst] += 1
            
        dp = [[0]*26 for _ in range(n)]
        
        q = deque([])
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
                dp[i][ord(colors[i]) - ord("a")] = 1
        
        res, seen = 0, 0
        
        while q:
            src = q.popleft()
            seen += 1
            value = max(dp[src])
            res = max(res, value)
            if src in graph:
                for dst in graph[src]:
                    for i in range(26):
                        dp[dst][i] = max(dp[dst][i], dp[src][i])
                    degree[dst] -= 1
                    if degree[dst] == 0:
                        dp[dst][ord(colors[dst]) - ord("a")] += 1
                        q.append(dst)
                        
        if seen == n:
            return res
        else:
            return -1