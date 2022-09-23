class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        
        def dfs(path, i):
            if i == len(graph) - 1:
                res.append(path)
                return
            for j in graph[i]:
                dfs(path + [j], j)
        
        dfs([0], 0)
        return res