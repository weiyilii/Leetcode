class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for to in graph[node]:
                indegree[to] -= 1
                if indegree[to] == 0:
                    q.append(to)
        
        return res if len(res) == numCourses else []
