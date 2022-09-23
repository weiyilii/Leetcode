class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(set)
        for edge in prerequisites:
            src, dst = edge
            graph[src].add(dst)
            
        visited = [False]*numCourses
        onPath = [False]*numCourses
        self.hasCycle = False
        
        def dfs(i):
            if onPath[i]:
                self.hasCycle = True
            if visited[i] or onPath[i]:
                return
            onPath[i] = True
            visited[i] = True
            for j in graph[i]:
                dfs(j)
            onPath[i] = False
        
        for i in range(numCourses):
            dfs(i)
        
        return False if self.hasCycle else True