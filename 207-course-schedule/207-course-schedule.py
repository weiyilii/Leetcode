class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        
        graph = collections.defaultdict(set)
        indegree = [0]*numCourses
        for [dst, src] in prerequisites:
            graph[src].add(dst)
            indegree[dst] += 1
        
        q = deque()
        for node, degree in enumerate(indegree):
            if degree == 0:
                q.append(node)
                
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for to in graph[node]:
                indegree[to] -= 1
                if indegree[to] == 0:
                    q.append(to)
        
        return count == numCourses