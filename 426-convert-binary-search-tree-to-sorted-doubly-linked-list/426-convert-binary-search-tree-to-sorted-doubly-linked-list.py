"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        self.first, self.last = None, None
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.last:
                node.left = self.last
                self.last.right = node
            else:
                self.first = node
            self.last = node
            dfs(node.right)
        
        dfs(root)
        self.first.left = self.last
        self.last.right = self.first
        
        return self.first