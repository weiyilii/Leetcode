"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        copy = Node(node.val)
        visited = [None for i in range(101)]
        self.dfs(node, copy, visited)
        return copy
        
    def dfs(self, node, copy, visited):
        visited[copy.val] = copy
        
        for n in node.neighbors:
            if visited[n.val] is None:
                new = Node(n.val)
                copy.neighbors.append(new)
                self.dfs(n, new, visited)
            else:
                copy.neighbors.append(visited[n.val])