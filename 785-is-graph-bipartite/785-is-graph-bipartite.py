class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        self.isbp = True
        visited = set()
        color = [False]*n
        
        def dfs(i):
            if not self.isbp:
                return
            visited.add(i)
            for j in graph[i]:
                if j in visited:
                    if color[i] == color[j]:
                        self.isbp = False
                        return
                else:
                    color[j] = False if color[i] else True
                    dfs(j)
        
        for i in range(n):
            dfs(i)
            
        return self.isbp