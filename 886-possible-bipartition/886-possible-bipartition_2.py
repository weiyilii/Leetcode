class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # BFS
        from collections import deque
        
        graph = collections.defaultdict(set)
        for [a, b] in dislikes:
            graph[a].add(b)
            graph[b].add(a)
        
        visited = [False]*(n + 1)
        color = [False]*(n + 1)
        self.bp = True
        
        def bfs(i):
            visited[i] = True
            q = deque()
            q.append(i)
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if visited[v]:
                        if color[u] == color[v]:
                            self.bp = False
                            return
                    else:
                        color[v] = False if color[u] else True
                        visited[v] = True
                        q.append(v)
        
        for i in range(1, n+1):
            if not visited[i]:
                bfs(i)
        
        return self.bp
