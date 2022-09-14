"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
# Iterative Stack
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        stack = []
        cur = root
        first, last = None, None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if last:
                cur.left = last
                last.right = cur
            else:
                first = cur
            last = cur
            cur = cur.right
        first.left = last
        last.right = first
        return first
        
