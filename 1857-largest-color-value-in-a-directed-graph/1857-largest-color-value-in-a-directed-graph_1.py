class Solution(object):
    def largestPathValue(self, colors, edges):
        """
        :type colors: str
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import deque
        
        # graph is the adjency list
        graph = {}
        n = len(colors)
        # degree[i] = how many edges that ends with i
        degree = [0]*n
        
        for src, dst in edges:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
            degree[dst] += 1
        
        # dp[i][j] = max count of color j (j = color - "a") in all paths that ends with i
        dp = [[0]*26 for _ in range(n)]
        
        q = deque([])
        for i in range(n):
            # Initialize q by appending nodes that can only be starting points
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
                    # everytime meets dst, degree[dst] -= 1
                    # when degree[dst] == 0, means visited all edges end with dst
                    # now can append dst to queue and add dst's own color to dp
                    degree[dst] -= 1
                    if degree[dst] == 0:
                        dp[dst][ord(colors[dst]) - ord("a")] += 1
                        q.append(dst)
                        
        if seen == n:
            return res
        else:
            return -1
