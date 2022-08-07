class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visited = [0 for i in range(numCourses)]
        # Create graph as adjacency list
        graph = [[] for i in range(numCourses)]
        for [x, y] in prerequisites:
            graph[y].append(x)
        
        for i in range(numCourses):
            if not self.dfs(i, graph, visited):
                return False
        return True
    
    def dfs(self, i, graph, visited):
        # Mark node being visited as -1
        # Mark node has been visited as 1
        # in each dfs, if a node is -1, that means it is being visited before, a cycle is found
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(j, graph, visited):
                return False
        # After finishing dfs this node, mark it as 1
        visited[i] = 1
        return True
