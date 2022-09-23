class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph  = collections.defaultdict(set)
        for [dst, src] in prerequisites:
            graph[src].add(dst)
        
        postorder = []
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
            postorder.append(i)
        
        for i in range(numCourses):
            dfs(i)
        return [] if self.hasCycle else postorder[::-1]