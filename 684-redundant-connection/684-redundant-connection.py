class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for neighbor in graph[source]:
                    if dfs(neighbor, target):
                        return True
                return False
        
        for source, target in edges:
            seen = set()
            if source in graph and target in graph and dfs(source, target):
            #if dfs(source, target):
                return [source, target]
            graph[source].add(target)
            graph[target].add(source)