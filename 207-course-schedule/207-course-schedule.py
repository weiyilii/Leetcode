class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        for [x, y] in prerequisites:
            graph[y].append(x)
        
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return False
        return True
    
    def dfs(self, i, graph, visited):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(j, graph, visited):
                return False
        visited[i] = 1
        return True