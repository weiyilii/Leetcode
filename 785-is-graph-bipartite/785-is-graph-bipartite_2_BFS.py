class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        
        n = len(graph)
        visited = set()
        color = [False]*n
        self.isbp = True
        
        def bfs(i):
            visited.add(i)
            q = deque()
            q.append(i)
            while q:
                node = q.popleft()
                for j in graph[node]:
                    if j in visited:
                        if color[node] == color[j]:
                            self.isbp = False
                            return
                    else:
                        color[j] = False if color[node] else True
                        visited.add(j)
                        q.append(j)
        
        for i in range(n):
            if i not in visited:
                bfs(i)
        print(color)
        return self.isbp
