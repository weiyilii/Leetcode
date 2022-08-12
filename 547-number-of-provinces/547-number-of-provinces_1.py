class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # DFS
        # Use visited (a list of boolean) to track if we have visited this city
        n = len(isConnected)
        visited = [False]*n
        
        def dfs(i):
            # Given i, check each j (!= i), if isConnected[i][j] is 1
            # If so, update visited[j] as True
            # Continue dfs with this j
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)
                    
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        return res
