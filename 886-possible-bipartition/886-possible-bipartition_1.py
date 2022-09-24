class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # DFS
     
        graph = collections.defaultdict(set)
        for [a, b] in dislikes:
            graph[a].add(b)
            graph[b].add(a)
            
        visited = [False]*n
        color = [False]*n
        self.bp = True
        
        def dfs(i):
            visited[i-1] = True
            for j in graph[i]:
                if visited[j-1]:
                    if color[i-1] == color[j-1]:
                        self.bp = False
                        return
                else:
                    color[j-1] = False if color[i-1] else True
                    dfs(j)
        
        for i in range(1, n+1):
            if not visited[i-1]:
                dfs(i)
        
        return self.bp
