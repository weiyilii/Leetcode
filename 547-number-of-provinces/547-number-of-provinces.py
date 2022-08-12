class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False]*n
        
        def dfs(i):
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