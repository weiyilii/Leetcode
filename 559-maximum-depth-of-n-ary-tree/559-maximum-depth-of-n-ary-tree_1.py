"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """  
        # DFS
        if not root:
            return 0
        # If initialize depth as float('-inf'), then be careful when node does not have children, depth will not be updated
        # But use intial depth as 0, even no children, 0 is correct.
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return depth + 1
