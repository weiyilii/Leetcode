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
        self.first, self.last = None, None
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            if self.last:
                self.last.right = root
                root.left = self.last
            else:
                self.first = root
            self.last = root
            dfs(root.right)
            
        if not root:
            return
        dfs(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first
        