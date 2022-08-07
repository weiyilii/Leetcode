class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited = [0 for i in range(numCourses)]
        stack = []
        graph = [[] for i in range(numCourses)]
        for [x, y] in prerequisites:
            graph[y].append(x)
        for i in range(numCourses):
            if not self.dfs(i, graph, visited, stack):
                return []
        return stack[::-1]
    
    def dfs(self, i, graph, visited, stack):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(j, graph, visited, stack):
                return False
        stack.append(i)
        visited[i] = 1
        return True