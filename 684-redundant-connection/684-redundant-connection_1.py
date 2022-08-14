class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # DFS
        # For each edge (source to target), use dfs to see if there is already a path from source to target using previously visited nodes in graph
        # If so, then this edge is duplicate
        graph = collections.defaultdict(set)
        
        def dfs(source, target):
            # When use dfs, may visit a node twice because u -> v and v -> u
            # Only when not seen source, continue checking
            if source not in seen:
                seen.add(source)
                # if source == target, means we have searched target, there is a path
                if source == target:
                    return True
                for neighbor in graph[source]:
                    if dfs(neighbor, target):
                        return True
                return False
        
        for source, target in edges:
            seen = set()
            # if dfs(source, target) is also acceptable but add if source in graph and target in graph can save some time
            if source in graph and target in graph and dfs(source, target):
                return [source, target]
            graph[source].add(target)
            graph[target].add(source)
